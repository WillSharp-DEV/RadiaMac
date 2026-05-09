# RadiaMac

RadiaMac is a unified, multiplatform companion application designed for real-time radiation analysis, spectrum visualization, and dosimetry logging. Built natively for macOS, iPadOS, and iOS, it connects to your local spectrometer server to provide live telemetry, peak identification, and historical data tracking through an intuitive, scalable interface.

## Core Features

* **Cross-Platform Support:** Seamlessly run your analysis on your Mac, iPad, or iPhone with adaptive UI layouts.
* **Spectrogram:** Time-series visualization with adjustable thermal coloring algorithms (Log, Linear, Sqrt).
* **Spectrum Graphing:** Live view of accumulated counts per channel with visual peak markers.
* **Live Telemetry Graphs:** Real-time plotting for Dosage, Counts per Second (CPS), and Accumulated Dosage.
* **Peak Identification:** Automated isotope identification based on detected energy peaks.
* **Sidebar Navigation & Detail Views:** Expand mini-charts from your dashboard into full-screen, high-resolution views.
* **Network & Server Configuration:** Connect to remote servers over your local Wi-Fi with custom IP routing and auto-scheme correction.
* **Health & Sync Monitoring:** Active connection tracking, background data loading overlays, and mid-analysis drop alerts.

---

## Visualizing Your Data

### Spectrogram
Includes features like thermal coloring settings (Log, Linear, Sqrt) and adjustable intensity multipliers to help visualize variations over time.

<img width="1350" height="938" alt="image" src="https://github.com/user-attachments/assets/bfb6c1ad-b674-4b48-b06f-bdcb27b22ee1" />


### Live Spectrum Graph
Visualization of accumulated counts per channel. Also includes a visual marker for all detected peaks for quick reference, alongside dynamic view range sliders.

Ipad Demonstration:
<img width="1376" height="1032" alt="Screenshot 2026-05-09 at 12 01 41 AM" src="https://github.com/user-attachments/assets/41493880-6b0b-4fa5-9324-97958eb1f6e9" />



### Telemetry & Tracking
Monitor your environment with dedicated graphs directly from the dashboard or in their own expanded views. Hover over a specific point in time to get an exact timestamp and its value at that moment.

**Dosage & Accumulated Dosage Graphs**
Toggle between live Dose Rate (µSv/h) and Total Accumulated Dose (µSv).

<img width="1350" height="938" alt="image" src="https://github.com/user-attachments/assets/61a8318d-2198-4b0e-bfbc-c9bb0827640e" />


**CPS Graph**
Track Live Counts per Second over time.

<img width="1350" height="938" alt="image" src="https://github.com/user-attachments/assets/3a3d52e0-0185-4859-9bcf-d9b9e54ed99d" />


### Peak Identification System
Automated peak detection cross-references known energy signatures to suggest potential isotopes, listed clearly on the dashboard.

<img width="1350" height="938" alt="image" src="https://github.com/user-attachments/assets/1855cd09-2247-482a-8721-0afc615f5e67" />


### Sidebar Navigation & Main Frame Expansion
Gone are the days of cluttered pop-up windows. RadiaMac utilizes a native sidebar to switch between your main dashboard and dedicated, high-resolution views for every chart. Click "Expand" on any dashboard widget to focus entirely on that data stream.

### Network Settings & Local Sync
RadiaMac is no longer tethered to the same machine running the server. Use the new Configuration menu to enter your server's local IP address and monitor your spectrometer from anywhere on your Wi-Fi network.

Ipad Demonstration:
<img width="1376" height="1032" alt="Screenshot 2026-05-09 at 12 05 38 AM" src="https://github.com/user-attachments/assets/24b7404f-eee0-4895-8473-dd01a015f54b" />


