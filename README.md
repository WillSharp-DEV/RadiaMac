# RadiaMac

RadiaMac is a macOS companion application designed for real-time radiation analysis, spectrum visualization, and dosimetry logging. It connects to your local spectrometer server to provide live telemetry, peak identification, and historical data tracking through an intuitive, native interface.

## Core Features

* **Spectrogram:** Time-series visualization with adjustable thermal coloring.
* **Spectrum Graphing:** Live view of accumulated counts per channel with visual peak markers.
* **Live Telemetry Graphs:** Real-time plotting for Dosage, Counts per Second (CPS), and Accumulated Dosage.
* **Peak Identification (WIP):** Automated isotope identification based on detected energy peaks.
* **Multi-Window Support:** Pop-out graphing capabilities for advanced, multi-monitor workspace management.
* **Server Health Monitoring:** Active connection tracking with persistent UI warnings and mid-analysis drop alerts.

---

## Visualizing Your Data

### Spectrogram
Includes features like thermal coloring settings (Log, Linear, Sqrt) to help visualize intensity variations over time.
<img width="1441" height="978" alt="Uranium sample spectrogram demonstration." src="https://github.com/user-attachments/assets/443db2c0-0e76-48e8-9627-f9989873493a" />


### Live Spectrum Graph
Visualization of accumulated counts per channel. Also includes a visual marker for all detected peaks for quick reference.
<img width="1441" height="978" alt="Uranium spectrum graph demonstration." src="https://github.com/user-attachments/assets/59a6612f-646c-42a4-a673-8caf08ee796e" />

### Telemetry & Tracking
Monitor your environment with dedicated graphs. Hover over a specific point in time to get an exact timestamp and its value at that moment.

**Dosage Graph**
<img width="907" height="563" alt="Dosage graph." src="https://github.com/user-attachments/assets/8420e01c-4a1a-4c18-83da-847d28478046" />

**CPS Graph**
<img width="971" height="596" alt="CPS graph." src="https://github.com/user-attachments/assets/3d307f75-106f-44c0-b479-a9d987f97f87" />

**Accumulated Dosage Graph**
<img width="907" height="563" alt="Accumulated dosage graph." src="https://github.com/user-attachments/assets/f41b2d53-d8a9-4696-8275-f18eeea75f52" />

### Peak Identification System
Automated peak detection cross-references known energy signatures to suggest potential isotopes (e.g., Uranium sample shown below).
<img width="1441" height="978" alt="Uranium sample peak identification." src="https://github.com/user-attachments/assets/e9e256de-4f71-481c-8c9a-f1f835eaa433" />

### Multi-Window Pop-out Capabilities
Break out specific graphs into their own scalable windows to optimize your screen real estate and run concurrent analyses.
<img width="1076" height="745" alt="Demonstration of spectrum graph in windowed popup." src="https://github.com/user-attachments/assets/87b6634a-fce3-464f-ad24-731432da8ca0" />
<img width="1441" height="978" alt="Demonstration of spectrum graph in windowed popup." src="https://github.com/user-attachments/assets/f0a99122-83cf-4238-a4c9-5055ce912ca1" />
