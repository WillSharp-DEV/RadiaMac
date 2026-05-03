from radiacode import RadiaCode, RealTimeData
from typing import Dict, List
import json
from gamma_emissions_library import CreateSearch
import numpy as np
from scipy.signal import find_peaks
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed
import time

try:
    probeDevice = RadiaCode()
    probeDevice.spectrum_reset()
except Exception as e:
    print(f"Warning: Could not connect to RadiaCode at startup: {e}")

# --- SERVER CONFIGURATION ---
SPECTROGRAM_ACCUMULATION_TIME = 3
MAX_HISTORY = 3600
MAX_SPECTROGRAM_HISTORY = 1000
# ----------------------------

# --- GLOBAL IN-MEMORY STORE ---
cpsDict: List = []
dosageDict: List = []
accumulatedDosageDict: List = [] # NEW
server_spectrogram_history: List = []

latest_spectrum_data = {}
latest_device_value = {}

spectrogram_row_counter = 0
latest_spectrogram_row = []
total_accumulated_dose = 0.0 

async def device_poller():
    global cpsDict, dosageDict, accumulatedDosageDict, server_spectrogram_history
    global latest_spectrum_data, latest_device_value
    global spectrogram_row_counter, latest_spectrogram_row, total_accumulated_dose
    
    print("Started background device poller...")
    
    last_time = 0
    previous_spectrum_counts = []
    spectrogram_accumulator = []
    last_spectrogram_emit = 0
    
    while True:
        try:
            currentSpectrum = probeDevice.spectrum()
            currentSecond = currentSpectrum.duration.total_seconds()

            
            if currentSecond < last_time:
                cpsDict.clear()
                dosageDict.clear()
                accumulatedDosageDict.clear() # NEW
                total_accumulated_dose = 0.0  # NEW
                previous_spectrum_counts.clear()
                spectrogram_accumulator.clear()
                server_spectrogram_history.clear()
                last_spectrogram_emit = currentSecond
            last_time = currentSecond

            spectrumCounts: List[int] = currentSpectrum.counts
            
            
            if not previous_spectrum_counts or len(previous_spectrum_counts) != len(spectrumCounts):
                delta_counts = spectrumCounts
                spectrogram_accumulator = [0] * len(spectrumCounts)
            else:
                delta_counts = [max(0, curr - prev) for curr, prev in zip(spectrumCounts, previous_spectrum_counts)]
            
            previous_spectrum_counts = spectrumCounts.copy()

            if not spectrogram_accumulator or len(spectrogram_accumulator) != len(spectrumCounts):
                spectrogram_accumulator = [0] * len(spectrumCounts)
                
            for i, val in enumerate(delta_counts):
                spectrogram_accumulator[i] += val

            
            if (currentSecond - last_spectrogram_emit) >= SPECTROGRAM_ACCUMULATION_TIME:
                row_data = []
                for index, delta_val in enumerate(spectrogram_accumulator):
                    row_data.append({
                        "deltaCounts": delta_val,
                        "energy": (currentSpectrum.a0 + currentSpectrum.a1 * index + currentSpectrum.a2 * index ** 2)
                    })
                
                latest_spectrogram_row = row_data
                server_spectrogram_history.insert(0, row_data)
                
                server_spectrogram_history = server_spectrogram_history[:MAX_SPECTROGRAM_HISTORY]
                spectrogram_row_counter += 1
                
                spectrogram_accumulator = [0] * len(spectrumCounts)
                last_spectrogram_emit = currentSecond

            
            spectrumDict: List = []
            peaksDict: List = []

            for index, value in enumerate(spectrumCounts):
                spectrumDict.append({
                    "counts": value,
                    "energy": (currentSpectrum.a0 + currentSpectrum.a1 * index + currentSpectrum.a2 * index ** 2)
                })

            peaks, _ = find_peaks(np.array(spectrumCounts), prominence=15, width=5, height=10)
            
            for peak in peaks.tolist():
                isotopeNamesList = []
                itemEnergy = spectrumDict[peak]["energy"]
                for i in CreateSearch().Search.InRange(itemEnergy, 10):
                    isotopeNamesList.append(i.Name)
                peaksDict.append({
                    "energy": itemEnergy,
                    "counts": spectrumDict[peak]["counts"],
                    "isotopeNames": isotopeNamesList
                })

            
            try:
                currentTimeStamp = time.time() 
                for record in probeDevice.data_buf():
                    if isinstance(record, RealTimeData):
                        dose_rate = record.dose_rate * 10000
                        
                        cpsDict.append({
                            "time": currentSecond, 
                            "cps": record.count_rate, 
                            "absoluteTime": currentTimeStamp 
                        })
                        dosageDict.append({
                            "time": currentSecond, 
                            "dosage": dose_rate, 
                            "absoluteTime": currentTimeStamp 
                        })
                        
                        
                        total_accumulated_dose += dose_rate / 3600.0
                        accumulatedDosageDict.append({
                            "time": currentSecond,
                            "dosage": total_accumulated_dose,
                            "absoluteTime": currentTimeStamp
                        })
            except Exception as e:
                pass 

            cpsDict = cpsDict[-MAX_HISTORY:]
            dosageDict = dosageDict[-MAX_HISTORY:]
            accumulatedDosageDict = accumulatedDosageDict[-MAX_HISTORY:] 
            latest_spectrum_data = {
                "spectrum": spectrumDict,
                "a0": currentSpectrum.a0,
                "a1": currentSpectrum.a1,
                "a2": currentSpectrum.a2,
                "duration": currentSpectrum.duration.total_seconds(),
                "peaks": peaksDict
            }
            
            latest_device_value = {
                "dosage": dosageDict,
                "accumulatedDosage": accumulatedDosageDict, 
                "countRate": cpsDict,
                "serialNumber": probeDevice.serial_number()
            }

        except Exception as e:
            print(f"Background Poller encountered an error: {e}")
            
        await asyncio.sleep(1)


async def client_handler(websocket):
    """Handles an individual Swift client connection."""
    print("Client connected! Sending history...")
    is_first_packet = True
    local_row_counter = spectrogram_row_counter
    
    while True:
        try:
            
            if not latest_spectrum_data:
                await asyncio.sleep(0.5)
                continue

            DictReturn: Dict = {
                "spectrumData": latest_spectrum_data,
                "deviceValue": latest_device_value
            }
            
            if is_first_packet:
                
                DictReturn["spectrogramHistoryLoad"] = server_spectrogram_history
                is_first_packet = False
            elif local_row_counter != spectrogram_row_counter:
                
                DictReturn["spectrogramRow"] = latest_spectrogram_row
                local_row_counter = spectrogram_row_counter

            await websocket.send(json.dumps(DictReturn))
            await asyncio.sleep(1)

        except ConnectionClosed:
            print("Client disconnected.")
            break 
        except Exception as e:
            print(f"Client handler error: {e}")
            await asyncio.sleep(1)

async def main():
    
    asyncio.create_task(device_poller())
    
    print("RadiaMac Server Running. Waiting for Swift Client...")
    async with websockets.serve(client_handler, "localhost", 8945):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())