# RadiaMac

A macOS application for real-time gamma spectroscopy using RadiaCode devices. This project consists of a Python backend for hardware interfacing and data processing, and a native Swift frontend for visualization and control.

## Architecture Overview

The system is divided into two distinct components that communicate via a local WebSocket connection.

### Backend (Python)

The backend is responsible for all hardware communication and heavy mathematical processing.

* **Hardware Interface**: Connects to RadiaCode devices using the `radiacode` library.
* **WebSocket Server**: Hosts a local server on port 8945 to stream data to the frontend.
* **Spectrum Analysis**: Continuously acquires gamma spectrum data from the device.
* **Energy Calibration**: Applies polynomial calibration (a0, a1, a2) to convert raw channels into energy levels.
* **Peak Detection**: Uses `scipy.signal` and `numpy` to identify significant peaks in the spectrum.
* **Isotope Identification**: Matches detected peaks against a library of known gamma-emitting isotopes.
* **Dosimetry**: Tracks real-time Dose Rate and Count Rate (CPS).

### Frontend (macOS / Swift)

The frontend provides the user interface and data visualization.

<img width="1371" height="838" alt="image" src="https://github.com/user-attachments/assets/8bfd9014-ebae-495d-a3ea-0afdd044c65d" />

* **Native UI**: Built with SwiftUI for a responsive macOS experience.
* **Data Visualization**: Renders real-time spectral charts and data points.
* **Process Management**: Manages the lifecycle of the Python backend process.
* **Telemetry Display**: Shows device serial number, current dosage, and count rates.
* **Data Persistence**: Maintains a history of readings during the session.

## Requirements

* **macOS**: 12.0 or later.
* **Python**: 3.10 or later.
* **Python Dependencies**:
    * radiacode
    * numpy
    * scipy
    * websockets

## Usage

1.  Ensure the Python environment is set up with the required dependencies.
2.  The application uses a local WebSocket connection (ws://localhost:8945).
3.  The Swift application is designed to launch the Python backend automatically upon startup.
