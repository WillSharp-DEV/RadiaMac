import SwiftUI
import Starscream
import Charts
import Combine

// MARK: - Scale Enum
enum ColorScaleType: String, CaseIterable {
    case linear = "Linear"
    case sqroot = "Sqrt"
    case log = "Log"
}

// MARK: - Models
struct SpectrumGraph: Identifiable, Codable {
    let id = UUID()
    let counts: Double
    let energy: Double
    enum CodingKeys: String, CodingKey { case counts, energy }
}

struct SpectrogramGraphRow: Identifiable, Codable {
    let id = UUID()
    let deltaCounts: Double
    let energy: Double
    enum CodingKeys: String, CodingKey { case deltaCounts, energy }
}

struct CpsGraph: Identifiable, Codable {
    let id = UUID()
    let time: Double
    let cps: Double
    let absoluteTime: Double?
    enum CodingKeys: String, CodingKey { case time, cps, absoluteTime }
}

struct DosageGraph: Identifiable, Codable {
    let id = UUID()
    let time: Double
    let dosage: Double
    let absoluteTime: Double?
    enum CodingKeys: String, CodingKey { case time, dosage, absoluteTime }
}

struct PeakInfo: Identifiable, Codable {
    let id = UUID()
    let energy: Double
    let counts: Double
    let isotopeNames: [String]
    enum CodingKeys: String, CodingKey { case energy, counts, isotopeNames }
}

struct DeviceValues: Codable {
    let dosage: [DosageGraph]
    let accumulatedDosage: [DosageGraph]?
    let countRate: [CpsGraph]
    let serialNumber: String
}

struct SpectrumItem: Codable {
    let spectrum: [SpectrumGraph]
    let a0: Double
    let a1: Double
    let a2: Double
    let duration: Double
    let peaks: [PeakInfo]
}

struct DataReturnCodable: Codable {
    let spectrumData: SpectrumItem
    let deviceValue: DeviceValues
    let spectrogramRow: [SpectrogramGraphRow]?
    let spectrogramHistoryLoad: [[SpectrogramGraphRow]]?
}

// MARK: - Socket Manager
class SocketManager: ObservableObject, WebSocketDelegate {
    
    @Published var liveData = DataReturnCodable(
        spectrumData: SpectrumItem(spectrum: [], a0: 0, a1: 0, a2: 0, duration: 0, peaks: []),
        deviceValue: DeviceValues(dosage: [], accumulatedDosage: [], countRate: [], serialNumber: "Waiting..."),
        spectrogramRow: nil,
        spectrogramHistoryLoad: nil
    )
    
    @Published var spectrogramHistory: [[SpectrogramGraphRow]] = []
    
    @Published var isSpectrogramPoppedOut = false
    @Published var isCpsPoppedOut = false
    @Published var isDosagePoppedOut = false
    @Published var isSpectrumPoppedOut = false
    
    @Published var colorScale: ColorScaleType = .linear
    @Published var intensityMultiplier: Double = 1.0
    @Published var minEnergy: Double = 0
    @Published var maxEnergy: Double = 3000
    
    // NEW: Connection state variables for the UI
    @Published var isConnected = false
    @Published var showConnectionAlert = false
    @Published var connectionError: String = ""
    
    var webSocket: WebSocket?
    
    func getData() {
        if isConnected { return }
        var request = URLRequest(url: URL(string: "ws://localhost:8945")!)
        request.timeoutInterval = 1
        
        webSocket = WebSocket(request: request)
        webSocket?.delegate = self
        webSocket?.connect()
    }
    
    func didReceive(event: WebSocketEvent, client: any WebSocketClient) {
            switch event {
            case .connected(_):
                print("CONNECTED TO SOCKET")
                DispatchQueue.main.async {
                    self.isConnected = true
                    self.showConnectionAlert = false
                }
                
            // UPDATED: Now triggers the popup on an unexpected disconnect
            case .disconnected(let reason, let code):
                print("DISCONNECTED: \(reason) with code: \(code)")
                DispatchQueue.main.async {
                    // Only show the alert if we were previously connected (mid-analysis)
                    if self.isConnected {
                        self.connectionError = "Connection lost: \(reason). Please check the server."
                        self.showConnectionAlert = true
                    }
                    self.isConnected = false
                }
                
            case .error(let error):
                print("SOCKET ERROR: \(String(describing: error))")
                DispatchQueue.main.async {
                    // Show alert for socket errors as well
                    if self.isConnected {
                        self.connectionError = error?.localizedDescription ?? "The server became non-responsive. "
                        self.showConnectionAlert = true
                    }
                    self.isConnected = false
                }
                
            case .cancelled:
                DispatchQueue.main.async {
                    self.isConnected = false
                }
                
            case .text(let string):
                if let data = string.data(using: .utf8) {
                    do {
                        let decoder = JSONDecoder()
                        let toReturn = try decoder.decode(DataReturnCodable.self, from: data)
                        
                        DispatchQueue.main.async {
                            if toReturn.spectrumData.duration < self.liveData.spectrumData.duration {
                                self.spectrogramHistory.removeAll()
                            }
                            
                            self.liveData = toReturn
                            
                            if let historyLoad = toReturn.spectrogramHistoryLoad {
                                self.spectrogramHistory = historyLoad
                            } else if let incomingRow = toReturn.spectrogramRow {
                                self.spectrogramHistory.insert(incomingRow, at: 0)
                                if self.spectrogramHistory.count > 1000 {
                                    self.spectrogramHistory.removeLast()
                                }
                            }
                        }
                    } catch {
                        print("ERROR WITH SPECTRUM CODABLE: \(error)")
                    }
                }
            default:
                break
            }
        }
}


// MARK: - Main Content View
struct ContentView: View {
    @EnvironmentObject var socketData: SocketManager
    @Environment(\.openWindow) private var openWindow
    @State private var showSpectrogram = false

    var body: some View {
        VStack(spacing: 0) {
            
            // NEW: Persistent Interface Warning Banner
            if !socketData.isConnected {
                HStack {
                    Image(systemName: "exclamationmark.triangle.fill")
                        .font(.title2)
                    Text("Server is disconnected or non-responsive.")
                        .font(.headline)
                    Spacer()
                    Button("Reconnect") {
                        socketData.getData()
                    }
                    .buttonStyle(.borderedProminent)
                    .tint(.white)
                    .foregroundColor(.red)
                }
                .padding()
                .background(Color.red.opacity(0.8))
                .foregroundColor(.white)
            }
            
            HStack(spacing: 20) {
                VStack(alignment: .leading, spacing: 15) {
                    HStack {
                        StatBox(title: "Dosage (µSv/h)", value: String(format: "%.2f", socketData.liveData.deviceValue.dosage.last?.dosage ?? 0))
                        
                        if let accDose = socketData.liveData.deviceValue.accumulatedDosage?.last?.dosage {
                            StatBox(title: "Total (µSv)", value: String(format: "%.4f", accDose))
                        }
                        
                        StatBox(title: "CPS", value: String(format: "%.1f", socketData.liveData.deviceValue.countRate.last?.cps ?? 0))
                    }
                    
                    HStack {
                        Text("CPS Graph").font(.headline)
                        Spacer()
                        if !socketData.isCpsPoppedOut {
                            Button(action: {
                                socketData.isCpsPoppedOut = true
                                openWindow(id: "cpsWindow")
                            }) { Image(systemName: "macwindow.badge.plus") }.buttonStyle(.plain)
                        }
                    }
                    
                    if socketData.isCpsPoppedOut {
                        PlaceholderView(title: "CPS Graph")
                            .frame(height: 150)
                    } else {
                        CpsChartView().frame(height: 150)
                    }
                    
                    HStack {
                        Text("Dosage Graph").font(.headline)
                        Spacer()
                        if !socketData.isDosagePoppedOut {
                            Button(action: {
                                socketData.isDosagePoppedOut = true
                                openWindow(id: "dosageWindow")
                            }) { Image(systemName: "macwindow.badge.plus") }.buttonStyle(.plain)
                        }
                    }
                    
                    if socketData.isDosagePoppedOut {
                        PlaceholderView(title: "Dosage Graph")
                            .frame(height: 150)
                    } else {
                        DosageChartView().frame(height: 150)
                    }
                    
                    Text("Peak Information").font(.headline)
                    List {
                        ForEach(socketData.liveData.spectrumData.peaks.indices, id: \.self) { index in
                            let peak = socketData.liveData.spectrumData.peaks[index]
                            Text("[\(index)] \(String(format: "%.1f", peak.energy)) keV : \(peak.isotopeNames.joined(separator: ", "))")
                                .font(.system(size: 12))
                        }
                    }
                    .listStyle(.plain)
                }
                .frame(maxWidth: 300)
                
                VStack {
                    HStack {
                        Picker("Display Mode", selection: $showSpectrogram) {
                            Text("Spectrum").tag(false)
                            Text("Spectrogram").tag(true)
                        }
                        .pickerStyle(.segmented)
                        .frame(width: 250)
                        
                        Spacer()
                        
                        if showSpectrogram {
                            if !socketData.isSpectrogramPoppedOut {
                                SpectrogramControlsView()
                                Button(action: {
                                    socketData.isSpectrogramPoppedOut = true
                                    openWindow(id: "spectrogramWindow")
                                }) { Image(systemName: "macwindow.badge.plus"); Text("Pop Out") }.buttonStyle(.bordered).tint(.blue)
                            }
                        } else {
                            if !socketData.isSpectrumPoppedOut {
                                Button(action: {
                                    socketData.isSpectrumPoppedOut = true
                                    openWindow(id: "spectrumWindow")
                                }) { Image(systemName: "macwindow.badge.plus"); Text("Pop Out") }.buttonStyle(.bordered).tint(.blue)
                            }
                        }
                    }
                    .padding(.bottom, 10)
                    
                    if showSpectrogram {
                        if socketData.isSpectrogramPoppedOut {
                            PlaceholderView(title: "Spectrogram")
                                .frame(maxWidth: .infinity, maxHeight: .infinity)
                        } else {
                            SpectrogramCanvas(
                                history: socketData.spectrogramHistory,
                                scaleType: socketData.colorScale,
                                intensity: socketData.intensityMultiplier
                            ).clipShape(RoundedRectangle(cornerRadius: 8))
                        }
                    } else {
                        if socketData.isSpectrumPoppedOut {
                            PlaceholderView(title: "Live Spectrum")
                                .frame(maxWidth: .infinity, maxHeight: .infinity)
                        } else {
                            SpectrumChartView()
                        }
                    }
                }
            }
            .padding()
        }
        .onAppear {
            socketData.getData()
        }
        // NEW: Popup Alert for Connection Error
        .alert(isPresented: $socketData.showConnectionAlert) {
            Alert(
                title: Text("Connection Lost"),
                message: Text(socketData.connectionError),
                dismissButton: .default(Text("OK"))
            )
        }
    }
}

// MARK: - Extracted Chart Components (Reusable)

struct CpsChartView: View {
    @EnvironmentObject var socketData: SocketManager
    @State private var hoveredCpsTime: Double?
    
    var body: some View {
        Chart {
            ForEach(socketData.liveData.deviceValue.countRate) { item in
                LineMark(x: .value("Time", item.time), y: .value("CPS", item.cps))
            }
            if let hoveredTime = hoveredCpsTime, let item = nearestCps(to: hoveredTime) {
                RuleMark(x: .value("Time", item.time))
                    .lineStyle(StrokeStyle(lineWidth: 1, dash: [5]))
                    .foregroundStyle(.gray)
                    .annotation(position: .top) {
                        TooltipView(time: item.absoluteTime, label: "CPS", value: String(format: "%.1f", item.cps))
                    }
            }
        }
        .chartXScale(domain: safeDomain(for: socketData.liveData.deviceValue.countRate.map { $0.time }))
        .chartXSelection(value: $hoveredCpsTime)
    }
    
    func nearestCps(to time: Double) -> CpsGraph? {
        socketData.liveData.deviceValue.countRate.min(by: { abs($0.time - time) < abs($1.time - time) })
    }
}

struct DosageChartView: View {
    @EnvironmentObject var socketData: SocketManager
    @State private var hoveredDosageTime: Double?
    @AppStorage("showAccumulatedDose") private var showAccumulated: Bool = false
    
    var body: some View {
        VStack(spacing: 5) {
            
            HStack {
                Picker("View Mode", selection: $showAccumulated) {
                    Text("Rate (µSv/h)").tag(false)
                    Text("Accumulated (µSv)").tag(true)
                }
                .pickerStyle(.segmented)
                .labelsHidden()
                .frame(width: 250)
                
                Spacer()
            }
            .padding(.bottom, 5)
            
            let data = showAccumulated ? (socketData.liveData.deviceValue.accumulatedDosage ?? []) : socketData.liveData.deviceValue.dosage
            
            Chart {
                ForEach(data) { item in
                    LineMark(x: .value("Time", item.time), y: .value("Dosage", item.dosage))
                }
                if let hoveredTime = hoveredDosageTime, let item = nearestDosage(to: hoveredTime, in: data) {
                    RuleMark(x: .value("Time", item.time))
                        .lineStyle(StrokeStyle(lineWidth: 1, dash: [5]))
                        .foregroundStyle(.gray)
                        .annotation(position: .top) {
                            TooltipView(
                                time: item.absoluteTime,
                                label: showAccumulated ? "Total Dose" : "Dose Rate",
                                value: String(format: showAccumulated ? "%.4f µSv" : "%.3f µSv/h", item.dosage)
                            )
                        }
                }
            }
            .chartXScale(domain: safeDomain(for: data.map { $0.time }))
            .chartXSelection(value: $hoveredDosageTime)
        }
    }
    
    
    func nearestDosage(to time: Double, in data: [DosageGraph]) -> DosageGraph? {
        data.min(by: { abs($0.time - time) < abs($1.time - time) })
    }
}
struct SpectrumChartView: View {
    @EnvironmentObject var socketData: SocketManager
    
    var body: some View {
        VStack {
            Chart {
                ForEach(socketData.liveData.spectrumData.spectrum) { item in
                    LineMark(x: .value("Energy", item.energy), y: .value("Counts", item.counts))
                }
                ForEach(socketData.liveData.spectrumData.peaks.indices, id: \.self) { index in
                    let peak = socketData.liveData.spectrumData.peaks[index]
                    PointMark(x: .value("Energy", peak.energy), y: .value("Counts", peak.counts))
                        .foregroundStyle(.green)
                        .annotation(position: .top) { Text(String(index)).font(.caption) }
                }
            }
            .chartXScale(domain: socketData.minEnergy...max(socketData.minEnergy + 1, socketData.maxEnergy))
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            
            VStack(spacing: 5) {
                Text("Graph View Range").font(.subheadline).bold()
                HStack {
                    Text("Min: \(Int(socketData.minEnergy))")
                    Slider(value: $socketData.minEnergy, in: 0...max(0, socketData.maxEnergy - 10))
                    Text("Max: \(Int(socketData.maxEnergy))")
                    Slider(value: $socketData.maxEnergy, in: (socketData.minEnergy + 10)...3000)
                }
            }
            .padding(.top, 10)
        }
    }
}


func safeDomain(for values: [Double]) -> ClosedRange<Double> {
    let minVal = values.first ?? 0
    let maxVal = values.last ?? 1
    return minVal...max(minVal + 0.1, maxVal)
}

// MARK: - Reusable UI Widgets

struct PlaceholderView: View {
    let title: String
    var body: some View {
        VStack(spacing: 10) {
            Image(systemName: "macwindow.on.rectangle")
                .font(.system(size: 30))
                .foregroundColor(.secondary)
            Text("\(title) is open in a separate window.")
                .font(.caption)
                .foregroundColor(.secondary)
                .multilineTextAlignment(.center)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color.secondary.opacity(0.1))
        .cornerRadius(8)
    }
}

struct SpectrogramControlsView: View {
    @EnvironmentObject var socketData: SocketManager
    var body: some View {
        HStack {
            Picker("Scale", selection: $socketData.colorScale) {
                ForEach(ColorScaleType.allCases, id: \.self) { scale in Text(scale.rawValue).tag(scale) }
            }.pickerStyle(.segmented).frame(width: 150)
            HStack {
                Text("Int:").font(.caption).foregroundStyle(.secondary)
                Slider(value: $socketData.intensityMultiplier, in: 0.1...5.0).frame(width: 100)
            }
        }
    }
}

struct TooltipView: View {
    let time: Double?
    let label: String
    let value: String
    var formattedTime: String {
        guard let timestamp = time else { return "--:--" }
        let date = Date(timeIntervalSince1970: timestamp)
        let formatter = DateFormatter()
        formatter.timeStyle = .medium
        return formatter.string(from: date)
    }
    var body: some View {
            VStack(alignment: .leading, spacing: 2) {
                Text(formattedTime).font(.caption2).foregroundStyle(.secondary)
                HStack { Text("\(label):").font(.caption).bold(); Text(value).font(.caption) }
            }
            .padding(6)
            .background(.regularMaterial)
            .cornerRadius(6)
            .shadow(radius: 2)
        }
}

struct StatBox: View {
    let title: String
    let value: String
    var body: some View {
        VStack {
            Text(title).font(.caption).foregroundColor(.secondary)
            Text(value).font(.title2).bold()
        }
        .frame(maxWidth: .infinity).padding().background(Color.secondary.opacity(0.1)).cornerRadius(8)
    }
}

// MARK: - Pop Out Window Views

struct PopOutSpectrogramView: View {
    @EnvironmentObject var socketData: SocketManager
    
    var body: some View {
        VStack(spacing: 0) {
            
            HStack {
                Text("Live Spectrogram").font(.headline)
                Spacer()
                SpectrogramControlsView()
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 12)
            
            .fixedSize(horizontal: false, vertical: true)
            .background(Color(NSColor.windowBackgroundColor))
            
            
            SpectrogramCanvas(
                history: socketData.spectrogramHistory,
                scaleType: socketData.colorScale,
                intensity: socketData.intensityMultiplier
            )
        }
        .frame(minWidth: 500, minHeight: 400)
        
        .background(Color.black)
        .onDisappear { socketData.isSpectrogramPoppedOut = false }
    }
}

struct PopOutCpsView: View {
    @EnvironmentObject var socketData: SocketManager
    var body: some View {
        VStack(alignment: .leading) {
            Text("CPS Graph").font(.headline).padding([.top, .horizontal])
            CpsChartView().padding()
        }
        .frame(minWidth: 400, minHeight: 300)
        .onDisappear { socketData.isCpsPoppedOut = false }
    }
}

struct PopOutDosageView: View {
    @EnvironmentObject var socketData: SocketManager
    var body: some View {
        VStack(alignment: .leading) {
            Text("Dosage Graph").font(.headline).padding([.top, .horizontal])
            DosageChartView().padding()
        }
        .frame(minWidth: 400, minHeight: 300)
        .onDisappear { socketData.isDosagePoppedOut = false }
    }
}

struct PopOutSpectrumView: View {
    @EnvironmentObject var socketData: SocketManager
    var body: some View {
        VStack(alignment: .leading) {
            Text("Live Spectrum").font(.headline).padding([.top, .horizontal])
            SpectrumChartView().padding()
        }
        .frame(minWidth: 600, minHeight: 400)
        .onDisappear { socketData.isSpectrumPoppedOut = false }
    }
}

// MARK: - Spectrogram Canvas
struct SpectrogramCanvas: View {
    var history: [[SpectrogramGraphRow]]
    var scaleType: ColorScaleType
    var intensity: Double
    var body: some View {
        GeometryReader { geo in
            let columns = CGFloat(history.first?.count ?? 1)
            let squareSize = geo.size.width / columns
            let totalHeight = squareSize * CGFloat(history.count)
            ScrollView(.vertical) {
                Canvas { context, size in
                    guard !history.isEmpty else { return }
                    for (rowIndex, row) in history.enumerated() {
                        let y = CGFloat(rowIndex) * squareSize
                        for (colIndex, bin) in row.enumerated() {
                            let x = CGFloat(colIndex) * squareSize
                            if bin.deltaCounts <= 0 { continue }
                            var scaledValue: Double = 0
                            var baseThreshold: Double = 1.0
                            switch scaleType {
                            case .linear: scaledValue = bin.deltaCounts; baseThreshold = 15.0
                            case .sqroot: scaledValue = sqrt(bin.deltaCounts); baseThreshold = 4.0
                            case .log: scaledValue = log10(bin.deltaCounts + 1); baseThreshold = 1.5
                            }
                            let currentThreshold = baseThreshold / intensity
                            let normalized = min(scaledValue / currentThreshold, 1.0)
                            let hue = 0.66 - (0.66 * normalized)
                            let color = Color(hue: hue, saturation: 1.0, brightness: 1.0)
                            context.fill(Path(CGRect(x: x, y: y, width: squareSize + 0.5, height: squareSize + 0.5)), with: .color(color))
                        }
                    }
                }
                .frame(width: geo.size.width, height: max(geo.size.height, totalHeight))
                .background(Color.black)
            }
        }
    }
}
