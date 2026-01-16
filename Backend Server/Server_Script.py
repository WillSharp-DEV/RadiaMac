import xml.etree.ElementTree as ET
import datetime
import time
import json
import threading
import os
from http.server import BaseHTTPRequestHandler
from socketserver import ThreadingMixIn, TCPServer
from typing import Optional, Dict, Any
import argparse
import sys

import numpy as np
from radiacode import RadiaCode, Spectrum, RealTimeData


class Config:
    """Holds all user-configurable settings, passed in on initialization."""
    def __init__(self, args):
        # General Settings
        self.DEVICE_SERIAL = args.device_serial
        self.MEASUREMENT_SECONDS = args.measurement_seconds
        self.RESET_SPECTRUM = not args.no_reset
        self.RESET_DOSE = args.reset_dose

        # Server Settings
        self.HOST = "0.0.0.0"
        self.JSON_PORT, self.XML_PORT, self.RATES_PORT = 8000, 8001, 8002


def to_json(data: Dict[str, Any]) -> str:
    """Converts a dictionary to a JSON string."""
    def convert(o):
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, (datetime.datetime, datetime.date)):
            return o.isoformat()
        if isinstance(o, datetime.timedelta):
            return o.total_seconds()
        raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

    return json.dumps(data, indent=4, default=convert)

def to_spectrometer_xml(spectrum: Spectrum, start_time_iso: str, serial_number: str) -> str:
    """
    Converts spectrum data into the specific XML format matching the example file.
    """
    ET.register_namespace('xsd', "http://www.w3.org/2001/XMLSchema")
    ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
    root = ET.Element("ResultDataFile")
    ET.SubElement(root, "FormatVersion").text = "120920"
    result_data_list = ET.SubElement(root, "ResultDataList")
    result_data = ET.SubElement(result_data_list, "ResultData")
    dev_conf_ref = ET.SubElement(result_data, "DeviceConfigReference")
    ET.SubElement(dev_conf_ref, "Name").text = "RadiaCode-110"
    sample_info = ET.SubElement(result_data, "SampleInfo")
    spectrum_name_text = f"Spectrum {datetime.datetime.fromisoformat(start_time_iso).strftime('%Y-%m-%d %H:%M:%S')}"
    ET.SubElement(sample_info, "Name").text = spectrum_name_text
    ET.SubElement(sample_info, "Note")
    ET.SubElement(result_data, "BackgroundSpectrumFile")
    start_time = datetime.datetime.fromisoformat(start_time_iso)
    end_time = start_time + spectrum.duration
    ET.SubElement(result_data, "StartTime").text = start_time.isoformat(timespec='seconds')
    ET.SubElement(result_data, "EndTime").text = end_time.isoformat(timespec='seconds')
    energy_spectrum = ET.SubElement(result_data, "EnergySpectrum")
    ET.SubElement(energy_spectrum, "NumberOfChannels").text = str(len(spectrum.counts))
    ET.SubElement(energy_spectrum, "ChannelPitch").text = "1.0"
    ET.SubElement(energy_spectrum, "SpectrumName").text = spectrum_name_text
    ET.SubElement(energy_spectrum, "SerialNumber").text = serial_number
    energy_cal = ET.SubElement(energy_spectrum, "EnergyCalibration")
    ET.SubElement(energy_cal, "PolynomialOrder").text = "2"
    coeffs = ET.SubElement(energy_cal, "Coefficients")
    ET.SubElement(coeffs, "Coefficient").text = str(spectrum.a0)
    ET.SubElement(coeffs, "Coefficient").text = str(spectrum.a1)
    ET.SubElement(coeffs, "Coefficient").text = str(spectrum.a2)
    ET.SubElement(energy_spectrum, "MeasurementTime").text = str(int(spectrum.duration.total_seconds()))
    spec = ET.SubElement(energy_spectrum, "Spectrum")
    for count in spectrum.counts:
        ET.SubElement(spec, "DataPoint").text = str(count)
    ET.SubElement(result_data, "Visible").text = "true"
    pulse_coll = ET.SubElement(result_data, "PulseCollection")
    ET.SubElement(pulse_coll, "Format").text = "Base64 encoded binary"
    ET.SubElement(pulse_coll, "Pulses")
    return ET.tostring(root, encoding='unicode')



class RadiaCodeManager:
    """Manages connection and data acquisition from a RadiaCode device."""
    def __init__(self, serial_number: str):
        self.serial_number, self.rc = serial_number, None
    def connect(self) -> bool:
        try:
            self.rc = RadiaCode(self.serial_number)
            print(f"✅ Successfully connected to RadiaCode device {self.serial_number}"); return True
        except Exception as e:
            print(f"❌ Failed to connect to RadiaCode device: {e}"); return False
            
    def get_spectrum(self) -> Optional[Spectrum]:
        if self.rc:
            try: return self.rc.spectrum()
            except Exception as e: print(f"❌ Error reading spectrum: {e}")
        return None
        
    def get_rates(self) -> Optional[Dict[str, float]]:
        """Fetches the latest count rate and dose rate from the device."""
        if self.rc:
            try:
                data_packets = self.rc.data_buf()
                if not data_packets:
                    return None
                
                for packet in reversed(data_packets):
                    if isinstance(packet, RealTimeData):
                        raw_dose_rate = getattr(packet, 'dose_rate', 0.0)
                        scaled_dose_rate = raw_dose_rate * 10000.0
                        
                        return {
                            'cps': getattr(packet, 'count_rate', 0.0),
                            'dose_rate_uSv_h': scaled_dose_rate
                        }
                return None
            except Exception as e:
                print(f"❌ Error reading rates: {e}")
        return None

    def reset_spectrum(self):
        if self.rc:
            try: self.rc.spectrum_reset(); print("🔄 Spectrum has been reset on the device.")
            except Exception as e: print(f"❌ Error resetting spectrum: {e}")


class ThreadingTCPServer(ThreadingMixIn, TCPServer):
    daemon_threads = True
    def __init__(self, server_address, RequestHandlerClass, port_type: str, config: Config):
        super().__init__(server_address, RequestHandlerClass)
        self.port_type = port_type
        self.config = config
        self.spectrum_data: Dict[str, Any] = {}
        self.rates_data: Dict[str, Any] = {}
        self.live_spectrum: Optional[Spectrum] = None
        self.data_lock = threading.Lock()

class DataHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        server = self.server
        if not isinstance(server, ThreadingTCPServer):
            self.send_response(500); self.end_headers(); return
            
        with server.data_lock:
            if server.port_type == 'JSON':
                content = to_json(server.spectrum_data.copy())
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(content, "utf8"))
                
            elif server.port_type == 'XML':
                if server.live_spectrum and server.spectrum_data:
                    start_timestamp_iso = server.spectrum_data.get("timestamp")
                    if isinstance(start_timestamp_iso, str):
                        content = to_spectrometer_xml(server.live_spectrum, start_timestamp_iso, server.config.DEVICE_SERIAL)
                        self.send_response(200)
                        self.send_header('Content-type', 'application/xml')
                        self.end_headers()
                        self.wfile.write(bytes(content, "utf8"))
                    else:
                        self.send_error(500, "Error: Timestamp is missing or invalid.")
                else:
                    self.send_response(204) # No Content
                    self.end_headers()
                    
            elif server.port_type == 'RATES':
                content = to_json(server.rates_data.copy())
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(content, "utf8"))
    
    def log_message(self, format, *args):
        pass

def run_server(server: ThreadingTCPServer):
    server.serve_forever()


def main(config: Config):
    print("🚀 Starting RadiaCode Data System")
    
    DOSE_STATE_FILE = "accumulated_dose.json"
    accumulated_dose_uSv = 0.0
    if not config.RESET_DOSE:
        try:
            with open(DOSE_STATE_FILE, 'r') as f:
                data = json.load(f)
                accumulated_dose_uSv = data.get('accumulated_dose_uSv', 0.0)
            print(f"✅ Loaded accumulated dose: {accumulated_dose_uSv:.3f} µSv")
        except (FileNotFoundError, json.JSONDecodeError):
            print("ℹ️ No previous accumulated dose file found, starting from zero.")
    else:
        print("🔄 Accumulated dose has been reset to zero by user command.")
        
    rc_manager = RadiaCodeManager(config.DEVICE_SERIAL)
    if not rc_manager.connect(): 
        return

    servers = [
        ThreadingTCPServer((config.HOST, config.JSON_PORT), lambda *a, **kw: DataHandler(*a, **kw), 'JSON', config),
        ThreadingTCPServer((config.HOST, config.XML_PORT), lambda *a, **kw: DataHandler(*a, **kw), 'XML', config),
        ThreadingTCPServer((config.HOST, config.RATES_PORT), lambda *a, **kw: DataHandler(*a, **kw), 'RATES', config)
    ]
    
    for s in servers: 
        threading.Thread(target=run_server, args=(s,), daemon=True).start()
    
    print(f"\n📡 Servers started on http://{config.HOST}:")
    print(f"  - Port {config.JSON_PORT}: Spectrum (JSON)")
    print(f"  - Port {config.XML_PORT}: Spectrum (XML)")
    print(f"  - Port {config.RATES_PORT}: Live Rates (JSON)")
    
    if config.RESET_SPECTRUM:
        rc_manager.reset_spectrum()
    else:
        print("\n💡 Spectrum accumulation will continue from the device's current state.")

    print(f"\n🔄 Reading data every {config.MEASUREMENT_SECONDS} seconds... (Press Ctrl+C to stop)\n")

    try:
        while True:
            spectrum = rc_manager.get_spectrum()
            rates = rc_manager.get_rates()
            
            if spectrum and rates:
                timestamp = datetime.datetime.now().isoformat()
                total_seconds = spectrum.duration.total_seconds()
                
                channels = np.arange(len(spectrum.counts))
                energies = spectrum.a0 + spectrum.a1 * channels + spectrum.a2 * channels**2
                current_spectrum_data = {
                    "timestamp": timestamp, "live_time_ms": total_seconds * 1000, 
                    "counts": spectrum.counts, "energies_keV": energies
                }
                
                dose_rate_uSv_h = rates.get('dose_rate_uSv_h', 0.0)
                cps = rates.get('cps', 0.0)
                dose_this_interval = (dose_rate_uSv_h / 3600.0) * config.MEASUREMENT_SECONDS
                accumulated_dose_uSv += dose_this_interval
                
                current_rates_data = {
                    "timestamp": timestamp,
                    "cps": cps,
                    "microsieverts_per_hour": dose_rate_uSv_h,
                    "accumulated_microsieverts": accumulated_dose_uSv
                }
                
                for server in servers:
                    with server.data_lock:
                        server.spectrum_data = current_spectrum_data
                        server.live_spectrum = spectrum
                        server.rates_data = current_rates_data

                print(f"\r🕐 Acquired: {total_seconds:7.1f}s | ⚡ CPS: {cps:7.2f} | ☢️ Rate: {dose_rate_uSv_h:7.3f} µSv/h | 📈 Total: {accumulated_dose_uSv:8.6f} µSv", end="")
            
            time.sleep(config.MEASUREMENT_SECONDS)
            
    except KeyboardInterrupt:
        print("\n\n🛑 User initiated shutdown (Ctrl+C).")
    finally:
        print(f"\n💾 Saving final accumulated dose: {accumulated_dose_uSv:.3f} µSv")
        try:
            with open(DOSE_STATE_FILE, 'w') as f:
                json.dump({'accumulated_dose_uSv': accumulated_dose_uSv}, f, indent=4)
        except Exception as e:
            print(f"❌ Could not save accumulated dose file: {e}")

        print("🛑 Shutting down servers...")
        for s in servers:
            try: s.shutdown(); s.server_close()
            except Exception as e: print(f"Warning: Error shutting down server: {e}")
        print("✅ Shutdown complete. Goodbye!")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RadiaCode Data Server", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    g_general = parser.add_argument_group('General Settings')
    g_general.add_argument('--device-serial', type=str, default="RC-110-001492", help="Device serial number.")
    g_general.add_argument('--measurement-seconds', type=int, default=1, help="Interval for data reads.")
    g_general.add_argument('--no-reset', action='store_true', help="Do not reset the accumulated spectrum on startup.")
    g_general.add_argument('--reset-dose', action='store_true', help="Reset the accumulated dose counter to zero on startup.")
    
    args = parser.parse_args()

    config_obj = Config(args)
    main(config_obj)