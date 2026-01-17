//
//  ContentView.swift
//  RadiaMac App
//
//  Created by William Sharp on 8/10/25.
//  Last Updated: 8/26/25
//

import SwiftUI
import Charts
import Combine
#if canImport(AppKit)
import AppKit
#endif

@MainActor
class AppSettings: ObservableObject {
    @AppStorage("accentColorData_v2") private var accentColorData: Data?
    @AppStorage("colorSchemeOption") private var colorSchemeName: String = ColorSchemeOption.system.rawValue

    @Published var accentColor: Color
    @Published var colorSchemeOption: ColorSchemeOption

    private var cancellables = Set<AnyCancellable>()

    init() {
        let savedColorData = UserDefaults.standard.data(forKey: "accentColorData_v2")
        let savedColorSchemeName = UserDefaults.standard.string(forKey: "colorSchemeOption") ?? ColorSchemeOption.system.rawValue
        
        self.accentColor = AppSettings.loadColor(from: savedColorData)
        self.colorSchemeOption = ColorSchemeOption(rawValue: savedColorSchemeName) ?? .system
        
        $accentColor.dropFirst().sink { [weak self] newColor in
            self?.accentColorData = AppSettings.saveColor(color: newColor)
        }.store(in: &cancellables)
        
        $colorSchemeOption.dropFirst().sink { [weak self] newScheme in
            self?.colorSchemeName = newScheme.rawValue
        }.store(in: &cancellables)
    }
    
    private static func saveColor(color: Color) -> Data {
        if let cgColor = color.cgColor, let components = cgColor.components, components.count >= 3 {
            let colorData: [CGFloat] = [components[0], components[1], components[2], cgColor.alpha]
            return colorData.withUnsafeBufferPointer { Data(buffer: $0) }
        }
        return Data()
    }
    
    private static func loadColor(from data: Data?) -> Color {
        guard let data = data, data.count >= MemoryLayout<CGFloat>.size * 4 else { return .cyan }
        let components = data.withUnsafeBytes { Array($0.bindMemory(to: CGFloat.self)) }
        if components.count >= 4 {
            return Color(red: components[0], green: components[1], blue: components[2], opacity: components[3])
        }
        return .cyan
    }
}

enum ColorSchemeOption: String, CaseIterable, Identifiable {
    case light = "Light", dark = "Dark", system = "System"
    var id: Self { self }
    var preferredColorScheme: ColorScheme? {
        switch self {
        case .light: return .light
        case .dark: return .dark
        case .system: return nil
        }
    }
}



struct SpectrumResponse: Codable {
    let timestamp: String, liveTimeMs: Double, counts: [Int], energiesKev: [Double]
    enum CodingKeys: String, CodingKey {
        case timestamp, counts, liveTimeMs = "live_time_ms", energiesKev = "energies_keV"
    }
}


struct RatesResponse: Codable {
    let timestamp: String, cps: Double, microsievertsPerHour: Double, accumulatedMicrosieverts: Double
    enum CodingKeys: String, CodingKey {
        case timestamp, cps, microsievertsPerHour = "microsieverts_per_hour", accumulatedMicrosieverts = "accumulated_microsieverts"
    }
}


struct IsotopeLibrary: Codable {
    let isotopes: [ParentIsotope]
}

struct ParentIsotope: Codable, Identifiable {
    var id: String { parent_name }
    let parent_name: String
    let parent_is_natural: Bool
    let decay_chain_name: String
    let decay_products: [DecayProduct]
}

struct DecayProduct: Codable, Identifiable, Hashable {
    let id: Int
    let name: String
    let half_life: String
    let decay_events: [DecayEvent]
    
    
    func hash(into hasher: inout Hasher) {
        hasher.combine(id)
        hasher.combine(name)
    }
    
    
    static func == (lhs: DecayProduct, rhs: DecayProduct) -> Bool {
        lhs.id == rhs.id && lhs.name == rhs.name
    }
}

struct DecayEvent: Codable, Hashable {
    let particle_type: String
    let energy_keV: Double
}


struct SpectrumPoint: Identifiable, Equatable {
    let id: Int, count: Int, energy: Double
}


struct HoveredIsotopeInfo: Equatable {
    let parentChainName: String
    let hoveredProduct: DecayProduct
    let closestEnergy: Double
    let allProductsInChain: [DecayProduct]
}

enum ScaleType: String, CaseIterable, Identifiable {
    case linear = "Linear", log = "Log"
    var id: Self { self }
}


struct ConnectionStatus: Identifiable {
    var id: Int { port }
    var name: String, port: Int, isConnected: Bool = false, lastAttempt: String = "Never"
}


@MainActor
class SpectrumViewModel: ObservableObject {
    
    @Published var spectrumPoints: [SpectrumPoint] = []
    @Published var lastUpdated: String = "Never"
    @Published var liveTime: Double = 0
    
    
    @Published var cps: Double = 0.0
    @Published var doseRate: Double = 0.0
    @Published var accumulatedDose: Double = 0.0
    
    
    @Published var smoothingLevel: Double = 0 { didSet { applyTransformations() } }
    @Published var amplificationLevel: Double = 0 { didSet { applyTransformations() } }
    @Published var yScaleType: ScaleType = .log
    @Published var showCrosshairs: Bool = false
    @Published var isPaused: Bool = false
    
    
    @Published var xAxisMin: Double = 0
    @Published var xAxisMax: Double = 3000
    @Published var maxEnergy: Double = 3000
    
    
    @Published var showIsotopeHighlights: Bool = true
    @Published var showNaturalIsotopesOnly = false
    @Published var hoveredIsotopeInfo: HoveredIsotopeInfo? = nil
    private var allParentIsotopes: [ParentIsotope] = []
    
    
    @Published var connectionStatuses: [ConnectionStatus] = [
        ConnectionStatus(name: "Spectrum", port: 8000),
        ConnectionStatus(name: "XML Data", port: 8001),
        ConnectionStatus(name: "Live Rates", port: 8002)
    ]
    
    @Published var showConnectionLostAlert: Bool = false
    private var didShowConnectionAlert: Bool = false
    private var rawSpectrumPoints: [SpectrumPoint] = []
    private var timer: Timer?

    init() {
        loadIsotopeLibrary()
        Task {
            print("Waiting for Python server to initialize...")
            try? await Task.sleep(for: .seconds(1))
            await fetchAllData()
            startTimer()
        }
    }
    
    private func loadIsotopeLibrary() {
        
        guard let url = Bundle.main.url(forResource: "IsotopeLibrary", withExtension: "json", subdirectory: "Python") else {
            print("FATAL ERROR: IsotopeLibrary.json not found in the Python subdirectory.")
            return
        }
        do {
            let data = try Data(contentsOf: url)
            let library = try JSONDecoder().decode(IsotopeLibrary.self, from: data)
            self.allParentIsotopes = library.isotopes
            print("✅ Successfully loaded \(allParentIsotopes.count) parent isotopes from the library.")
        } catch {
            print("❌ Failed to load or parse IsotopeLibrary.json: \(error)")
        }
    }
    
    func startTimer() {
        self.timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { [weak self] _ in
            Task { await self?.fetchAllData() }
        }
    }
    
    private func fetchAllData() async {
        guard !isPaused else { return }
        await fetchSpectrumData()
        await fetchRatesData()
    }
    
    func togglePause() { isPaused.toggle() }
    
    func resetZoom() {
        xAxisMin = 0
        xAxisMax = maxEnergy
    }
    
    
    func findClosestIsotope(at energy: Double) {
        let tolerance = 20.0
        
        
        let filteredParents = allParentIsotopes.filter { !showNaturalIsotopesOnly || $0.parent_is_natural }
        
        var closestMatch: (parent: ParentIsotope, product: DecayProduct, energy: Double)? = nil
        var minDistance = tolerance
        
        
        for parent in filteredParents {
            for product in parent.decay_products {
                for event in product.decay_events where event.particle_type == "Gamma" {
                    let distance = abs(event.energy_keV - energy)
                    if distance < minDistance {
                        minDistance = distance
                        closestMatch = (parent, product, event.energy_keV)
                    }
                }
            }
        }
        
        
        let newInfo: HoveredIsotopeInfo?
        if let match = closestMatch {
            newInfo = HoveredIsotopeInfo(
                parentChainName: match.parent.decay_chain_name,
                hoveredProduct: match.product,
                closestEnergy: match.energy,
                allProductsInChain: match.parent.decay_products
            )
        } else {
            newInfo = nil
        }

        if self.hoveredIsotopeInfo != newInfo {
            self.hoveredIsotopeInfo = newInfo
        }
    }
    
    private func updateConnectionStatus(port: Int, isConnected: Bool) {
        if let index = connectionStatuses.firstIndex(where: { $0.port == port }) {
            connectionStatuses[index].isConnected = isConnected
            connectionStatuses[index].lastAttempt = Date().formatted(.dateTime.hour().minute().second())
            if port == 8000 {
                if isConnected { didShowConnectionAlert = false }
                else if !didShowConnectionAlert { showConnectionLostAlert = true; didShowConnectionAlert = true }
            }
        }
    }
    
    func fetchSpectrumData() async {
        guard let url = URL(string: "http://127.0.0.1:8000") else { return }
        do {
            let (data, _) = try await URLSession.shared.data(from: url)
            let response = try JSONDecoder().decode(SpectrumResponse.self, from: data)
            let newPoints = response.counts.enumerated().compactMap { (index, count) -> SpectrumPoint? in
                guard index < response.energiesKev.count else { return nil }
                return SpectrumPoint(id: index, count: count, energy: response.energiesKev[index])
            }
            if self.rawSpectrumPoints != newPoints {
                self.rawSpectrumPoints = newPoints
                applyTransformations()
            }
            
            let newMaxEnergy = rawSpectrumPoints.last?.energy ?? 3000
            if self.maxEnergy != newMaxEnergy {
                let wasAtMax = (self.xAxisMax == self.maxEnergy)
                self.maxEnergy = newMaxEnergy
                if wasAtMax || self.xAxisMax == 3000 {
                    self.xAxisMax = newMaxEnergy
                }
            }
            
            self.liveTime = response.liveTimeMs / 1000.0
            self.lastUpdated = Date().formatted(.dateTime.hour().minute().second())
            updateConnectionStatus(port: 8000, isConnected: true)
        } catch { updateConnectionStatus(port: 8000, isConnected: false) }
    }
    
    func fetchRatesData() async {
        guard let url = URL(string: "http://127.0.0.1:8002") else { return }
        do {
            let (data, _) = try await URLSession.shared.data(from: url)
            let response = try JSONDecoder().decode(RatesResponse.self, from: data)
            self.cps = response.cps
            self.doseRate = response.microsievertsPerHour
            self.accumulatedDose = response.accumulatedMicrosieverts
            updateConnectionStatus(port: 8002, isConnected: true)
        } catch {
            updateConnectionStatus(port: 8002, isConnected: false)
        }
    }
    
    func downloadXMLData() async {
        guard let url = URL(string: "http://127.0.0.1:8001") else { return }
        do {
            let (data, _) = try await URLSession.shared.data(from: url)
            updateConnectionStatus(port: 8001, isConnected: true)
            let savePanel = NSSavePanel()
            savePanel.allowedContentTypes = [.xml]
            savePanel.nameFieldStringValue = "spectrum-\(Int(Date().timeIntervalSince1970)).xml"
            if savePanel.runModal() == .OK, let url = savePanel.url {
                try? data.write(to: url)
            }
        } catch { updateConnectionStatus(port: 8001, isConnected: false) }
    }
    
    private func applyTransformations() {
        var processedPoints = rawSpectrumPoints

        if amplificationLevel > 0 {
            processedPoints = processedPoints.map { point in
                let amplifiedCount = Double(point.count) + (log1p(Double(point.count)) * amplificationLevel)
                return SpectrumPoint(id: point.id, count: Int(amplifiedCount.rounded()), energy: point.energy)
            }
        }

        if smoothingLevel > 0 {
            let windowSize = Int(smoothingLevel) * 2 + 1
            let halfWindow = windowSize / 2
            self.spectrumPoints = processedPoints.indices.map { i in
                let start = max(0, i - halfWindow)
                let end = min(processedPoints.count - 1, i + halfWindow)
                let window = processedPoints[start...end]
                let avgCount = window.reduce(0) { $0 + $1.count } / window.count
                return SpectrumPoint(id: i, count: avgCount, energy: processedPoints[i].energy)
            }
        } else {
            self.spectrumPoints = processedPoints
        }
    }
    
    deinit { timer?.invalidate() }
}


struct ContentView: View {
    @StateObject private var settings = AppSettings()
    @StateObject private var viewModel = SpectrumViewModel()
    @State private var selectedTab: Tab = .spectrum
    
    enum Tab: String, CaseIterable {
        case spectrum = "chart.bar.xaxis", connections = "wifi", info = "info.circle", settings = "gear"
        var id: String { self.rawValue }
    }
    
    var body: some View {
        HStack(spacing: 0) {
            VStack {
                ForEach(Tab.allCases, id: \.id) { tab in
                    Button(action: { selectedTab = tab }) {
                        Image(systemName: tab.rawValue).font(.title2)
                            .symbolVariant(selectedTab == tab ? .fill : .none)
                            .frame(width: 50, height: 45)
                            .contentShape(Rectangle())
                    }
                    .buttonStyle(.plain)
                    .foregroundColor(selectedTab == tab ? settings.accentColor : .secondary)
                    .background(settings.accentColor.opacity(selectedTab == tab ? 0.25 : 0).animation(.spring(), value: selectedTab))
                    .cornerRadius(8).padding(.horizontal, 5)
                }
                Spacer()
            }
            .padding(.vertical, 5)
            
            Divider()
            
            Group {
                switch selectedTab {
                case .spectrum: SpectrumView(viewModel: viewModel)
                case .connections: ConnectionsView(viewModel: viewModel)
                case .info: InfoView()
                case .settings: SettingsView()
                }
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)
        }
        .environmentObject(settings)
        .accentColor(settings.accentColor)
        .preferredColorScheme(settings.colorSchemeOption.preferredColorScheme)
        .alert("Connection Lost", isPresented: $viewModel.showConnectionLostAlert) { Button("OK") {} }
    }
}


struct SpectrumView: View {
    @ObservedObject var viewModel: SpectrumViewModel
    
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HeaderView(viewModel: viewModel)
            LiveStatsView(viewModel: viewModel)
            SpectrumChartView(viewModel: viewModel)
            Divider()
            ControlsView(viewModel: viewModel)
        }.padding()
    }
}


struct LiveStatsView: View {
    @ObservedObject var viewModel: SpectrumViewModel
    
    var body: some View {
        HStack {
            StatBox(label: "CPS", value: String(format: "%.2f", viewModel.cps), unit: "counts/sec")
            Divider()
            StatBox(label: "Dose Rate", value: String(format: "%.3f", viewModel.doseRate), unit: "µSv/h")
            Divider()
            StatBox(label: "Total Dose", value: String(format: "%.6f", viewModel.accumulatedDose), unit: "µSv")
        }
        .frame(height: 60)
        .padding(.horizontal)
        .background(Color.primary.opacity(0.05))
        .cornerRadius(8)
    }
}

struct StatBox: View {
    let label: String, value: String, unit: String
    
    var body: some View {
        VStack(alignment: .leading) {
            Text(label).font(.caption).foregroundColor(.secondary)
            HStack(alignment: .firstTextBaseline, spacing: 4) {
                Text(value).font(.title2).fontWeight(.semibold).monospacedDigit()
                Text(unit).font(.caption).foregroundColor(.secondary)
            }
        }
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}


struct HeaderView: View {
    @ObservedObject var viewModel: SpectrumViewModel
    
    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                HStack {
                    Text("Live Spectrum").font(.title).fontWeight(.bold)
                    if viewModel.isPaused {
                        Text("PAUSED").font(.caption).fontWeight(.bold).padding(.horizontal, 8).padding(.vertical, 2)
                            .background(Color.orange).foregroundColor(.white).cornerRadius(4)
                    }
                }
                Text("Live Time: \(String(format: "%.1f", viewModel.liveTime))s • Last Updated: \(viewModel.lastUpdated)")
                    .font(.footnote).foregroundStyle(.secondary)
            }
            Spacer()
            Button(action: { Task { await viewModel.downloadXMLData() } }) {
                Label("Download XML", systemImage: "arrow.down.doc")
            }
        }
    }
}

struct ControlsView: View {
    @ObservedObject var viewModel: SpectrumViewModel
    
    var body: some View {
        HStack {
            Button(action: viewModel.togglePause) {
                Image(systemName: viewModel.isPaused ? "play.fill" : "pause.fill").font(.title2)
            }.buttonStyle(.plain).help(viewModel.isPaused ? "Resume updates" : "Pause updates")
            
            Divider().frame(height: 20).padding(.horizontal, 8)
            
            VStack(spacing: 12) {
                VStack(alignment: .leading) {
                    Text("Smoothing: \(Int(viewModel.smoothingLevel))").font(.headline)
                    Slider(value: $viewModel.smoothingLevel, in: 0...5, step: 1)
                }
                VStack(alignment: .leading) {
                    Text("Amplification: \(Int(viewModel.amplificationLevel))").font(.headline)
                    Slider(value: $viewModel.amplificationLevel, in: 0...20, step: 4)
                }
            }.frame(maxWidth: 200)
            
            Spacer()
            
            Picker("Isotope ID", selection: $viewModel.showIsotopeHighlights) {
                Text("Off").tag(false)
                Text("On").tag(true)
            }
            .pickerStyle(.segmented)
            .help("Enable or disable isotope peak highlighting on the chart.")
            
            Picker("Filter", selection: $viewModel.showNaturalIsotopesOnly) {
                Text("All").tag(false)
                Text("Natural").tag(true)
            }
            .pickerStyle(.segmented)
            .disabled(!viewModel.showIsotopeHighlights)
            .help(viewModel.showIsotopeHighlights ? "Filter for naturally occurring isotopes." : "Enable Isotope ID to use filter.")

            Picker("Y-Axis", selection: $viewModel.yScaleType) {
                ForEach(ScaleType.allCases) { Text($0.rawValue) }
            }.pickerStyle(.segmented)
            
            Toggle("Crosshairs", isOn: $viewModel.showCrosshairs).toggleStyle(.button)
        }.padding(.horizontal)
    }
}

struct InfoView: View {
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                Text("About RadiaMac").font(.largeTitle).fontWeight(.bold)
                Text("This application provides a real-time interface for the RadiaCode-110 gamma-ray spectrometer.").font(.title3)
                VStack(alignment: .leading, spacing: 10) {
                    Text("Features").font(.title2).fontWeight(.semibold)
                    Text("• **Live Spectrum:** View gamma-ray counts across a range of energy levels, updated every second.")
                    Text("• **Live Rate Data:** Monitor real-time Counts Per Second (CPS), dose rate, and total accumulated dose.")
                    Text("• **Isotope Highlighting:** Hover over the chart to see reference lines for known isotope energy peaks.")
                    Text("• **Interactive Chart:** Zoom, pan, and inspect the spectrum chart with crosshairs.")
                    Text("• **Data Export:** Download the raw spectrum data in a standard XML format for further analysis.")
                }
                Divider()
                VStack(alignment: .leading, spacing: 8) {
                    Text("A Note on Usage").font(.title2).fontWeight(.semibold)
                    Text("RadiaMac is designed as a powerful, modern data collection tool. For comprehensive analysis and report generation, we recommend exporting the data via the XML download feature for use in professional-grade software.")
                }
                Divider()
                Text("This interface was developed to provide a modern and responsive user experience for radiation hobbyists and professionals on macOS.").foregroundStyle(.secondary)
            }
            .padding(40).frame(maxWidth: 600)
        }
    }
}

struct SettingsView: View {
    @EnvironmentObject var settings: AppSettings
    var body: some View {
        Form {
            Section(header: Text("Appearance").font(.headline)) {
                Picker("Mode", selection: $settings.colorSchemeOption) {
                    ForEach(ColorSchemeOption.allCases) { Text($0.rawValue).tag($0) }
                }.pickerStyle(.segmented).padding(.bottom, 5)
                ColorPicker("Accent Color", selection: $settings.accentColor, supportsOpacity: false)
            }
        }.formStyle(.grouped).scrollContentBackground(.hidden).frame(maxWidth: 450).padding(40)
    }
}

struct ConnectionsView: View {
    @ObservedObject var viewModel: SpectrumViewModel

    var body: some View {
        VStack(alignment: .leading) {
            Text("Connection Status").font(.largeTitle).fontWeight(.bold).padding(.bottom, 10)
            List(viewModel.connectionStatuses) { status in
                VStack(alignment: .leading, spacing: 8) {
                    HStack {
                        Image(systemName: status.isConnected ? "checkmark.circle.fill" : "xmark.circle.fill").foregroundColor(status.isConnected ? .green : .red).font(.title2)
                        VStack(alignment: .leading) {
                            Text("\(status.name) (Port \(String(status.port)))").font(.headline)
                            Text("Last attempt: \(status.lastAttempt)").font(.caption).foregroundStyle(.secondary)
                        }
                        Spacer()
                        Text(status.isConnected ? "Connected" : "Disconnected").font(.callout).fontWeight(.semibold).foregroundColor(status.isConnected ? .green : .red)
                    }
                    if status.port == 8001 { Text("Status updates only after attempting to download XML data.").font(.caption2).foregroundStyle(.secondary).padding(.leading, 34) }
                }.padding(.vertical, 8)
            }.scrollContentBackground(.hidden)
        }.padding(40).frame(maxWidth: 500)
    }
}

struct ActivitySpectrogramView: View {
    let spectrumPoints: [SpectrumPoint], maxCount: Double
    var body: some View {
        Canvas { context, size in
            guard !spectrumPoints.isEmpty, maxCount > 0 else { return }
            let segmentWidth = size.width / Double(spectrumPoints.count)
            for (index, point) in spectrumPoints.enumerated() {
                let rect = CGRect(x: Double(index) * segmentWidth, y: 0, width: segmentWidth, height: size.height)
                context.fill(Path(rect), with: .color(colorFor(value: Double(point.count) / maxCount)))
            }
        }
    }
    private func colorFor(value: Double) -> Color {
        guard value > 0 else { return Color(hue: 0.7, saturation: 1.0, brightness: 0.5) }
        return Color(hue: 0.7 - (value * 0.7), saturation: 1.0, brightness: 1.0)
    }
}


struct SpectrumChartView: View {
    @ObservedObject var viewModel: SpectrumViewModel
    @EnvironmentObject var settings: AppSettings
    
    
    private var decayChainHighlightColor: Color { .orange }
    
    var body: some View {
        VStack(spacing: 4) {
            ActivitySpectrogramView(spectrumPoints: viewModel.spectrumPoints, maxCount: Double(viewModel.spectrumPoints.map(\.count).max() ?? 1))
                .frame(height: 20).clipShape(RoundedRectangle(cornerRadius: 4, style: .continuous)).padding(.bottom, 8)
            
            Chart {
                
                ForEach(viewModel.spectrumPoints) { point in
                    LineMark(x: .value("Energy", point.energy), y: .value("Counts", max(1, point.count)))
                }
                .foregroundStyle(by: .value("Data", "Spectrum"))
                
                
                
                if viewModel.showIsotopeHighlights, let info = viewModel.hoveredIsotopeInfo {
                    RuleMark(x: .value("Energy", info.closestEnergy))
                        .lineStyle(StrokeStyle(lineWidth: 2, dash: [5, 5]))
                        .foregroundStyle(settings.accentColor.highContrast)
                }
            }
            .clipped()
            .chartYScale(type: viewModel.yScaleType == .log ? .log : .linear)
            .chartYScale(domain: .automatic(includesZero: true))
            .chartXScale(domain: viewModel.xAxisMin...viewModel.xAxisMax)
            .chartYAxisLabel("Counts (\(viewModel.yScaleType.rawValue) Scale)").chartXAxisLabel("Energy (keV)")
            .chartForegroundStyleScale(["Spectrum": settings.accentColor])
            
            .chartOverlay { proxy in
                GeometryReader { geometry in
                    ChartOverlayLayer(viewModel: viewModel, proxy: proxy, geometry: geometry, settings: settings)
                }
            }
            .animation(.default, value: viewModel.spectrumPoints)
            
            ZoomRangeSlider(minValue: $viewModel.xAxisMin, maxValue: $viewModel.xAxisMax, range: 0...viewModel.maxEnergy, onReset: viewModel.resetZoom)
                .padding(.top, 8)
        }
    }
}

struct ChartOverlayLayer: View {
    @ObservedObject var viewModel: SpectrumViewModel
    let proxy: ChartProxy
    let geometry: GeometryProxy
    @ObservedObject var settings: AppSettings
    
    @State private var mouseLocation: CGPoint? = nil
    
    var body: some View {
        ZStack(alignment: .topLeading) {
            Color.clear.contentShape(Rectangle())
                .onContinuousHover { phase in
                    switch phase {
                    case .active(let loc):
                        mouseLocation = loc
                        let xValue: Double? = proxy.value(atX: loc.x)
                        if let energy = xValue {
                            if viewModel.showIsotopeHighlights {
                                viewModel.findClosestIsotope(at: energy)
                            }
                        }
                    case .ended:
                        mouseLocation = nil
                        viewModel.hoveredIsotopeInfo = nil
                    }
                }
            
            if viewModel.showIsotopeHighlights, let info = viewModel.hoveredIsotopeInfo {
                drawIsotopeLabels(info: info)
            }
            
            if viewModel.showCrosshairs, let loc = mouseLocation {
                drawCrosshairs(at: loc)
            }
        }
        .allowsHitTesting(true)
    }
    @ViewBuilder
    func drawIsotopeLabels(info: HoveredIsotopeInfo) -> some View {
        if let xPos = proxy.position(forX: info.closestEnergy) {
            Text("\(info.hoveredProduct.name)\n\(String(format: "%.1f", info.closestEnergy)) keV")
                .font(.caption).fontWeight(.bold)
                .multilineTextAlignment(.center)
                .padding(6)
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 6))
                .overlay(RoundedRectangle(cornerRadius: 6).stroke(Color.secondary.opacity(0.5)))
                .foregroundStyle(Color.primary)
                .position(x: xPos, y: 30)
                .allowsHitTesting(false)
        }

        ForEach(info.allProductsInChain.filter { $0 != info.hoveredProduct }, id: \.self) { other in
            ForEach(other.decay_events.filter { $0.particle_type == "Gamma" }, id: \.self) { event in
                if let xPos = proxy.position(forX: event.energy_keV) {
                    VStack(spacing: 0) {
                        Text(other.name)
                            .font(.system(size: 9, weight: .bold))
                            .padding(2)
                            .background(Color.orange.opacity(0.8))
                            .foregroundColor(.white)
                            .cornerRadius(3)
                        
                        Image(systemName: "arrowtriangle.up.fill")
                            .font(.caption2)
                            .foregroundColor(.orange)
                    }
                    .position(x: xPos, y: geometry.size.height - 20)
                    .allowsHitTesting(false)
                }
            }
        }
    }
    
    @ViewBuilder
    func drawCrosshairs(at location: CGPoint) -> some View {
        if let energy: Double = proxy.value(atX: location.x),
           let counts: Double = proxy.value(atY: location.y) {
            
            Rectangle()
                .fill(Color.gray.opacity(0.8))
                .frame(width: 1, height: geometry.size.height)
                .position(x: location.x, y: geometry.size.height / 2)
            

            Rectangle()
                .fill(Color.gray.opacity(0.8))
                .frame(width: geometry.size.width, height: 1)
                .position(x: geometry.size.width / 2, y: location.y)
            
            VStack(alignment: .leading, spacing: 2) {
                Text("E: \(String(format: "%.1f", energy)) keV")
                Text("C: \(Int(counts))")
            }
            .font(.caption2.monospacedDigit())
            .padding(4)
            .background(.regularMaterial)
            .cornerRadius(4)
            .position(x: location.x + 50, y: location.y - 20)
            .allowsHitTesting(false)
        }
    }
}

struct Crosshairs: View {
    let proxy: ChartProxy, location: CGPoint, plotAreaFrame: CGRect
    var body: some View {
        if let energy: Double = proxy.value(atX: location.x), let count: Double = proxy.value(atY: location.y) {
            
            let xPos = proxy.position(forX: energy) ?? 0
            let yPos = proxy.position(forY: count) ?? 0
            
            ZStack {
                
                Rectangle()
                    .fill(Color.secondary)
                    .frame(width: 1, height: plotAreaFrame.height)
                    .position(x: xPos, y: plotAreaFrame.midY)
                
                
                Rectangle()
                    .fill(Color.secondary)
                    .frame(width: plotAreaFrame.width, height: 1)
                    .position(x: plotAreaFrame.midX, y: yPos)
                
                
                Text(String(format: "%.1f keV", energy))
                    .font(.caption)
                    .padding(4)
                    .background(.ultraThinMaterial)
                    .cornerRadius(4)
                    .position(x: xPos, y: yPos - 25)
                    .fixedSize()
                
                
                Text("\(Int(count))")
                    .font(.caption)
                    .padding(4)
                    .background(.ultraThinMaterial)
                    .cornerRadius(4)
                    .position(x: xPos + 40, y: yPos)
                    .fixedSize()
            }
            .allowsHitTesting(false)
        }
    }
}


struct ZoomRangeSlider: View {
    @Binding var minValue: Double
    @Binding var maxValue: Double
    let range: ClosedRange<Double>
    let onReset: () -> Void
    
    var body: some View {
        HStack(spacing: 10) {
            Text("Zoom:").font(.caption).foregroundStyle(.secondary)
            Text("\(Int(minValue)) keV").font(.caption).monospacedDigit().frame(width: 60, alignment: .trailing)
            
            RangeSlider(minValue: $minValue, maxValue: $maxValue, range: range).frame(height: 20)
            
            Text("\(Int(maxValue)) keV").font(.caption).monospacedDigit().frame(width: 60, alignment: .leading)
            Button("Reset", action: onReset).font(.caption).buttonStyle(.plain).foregroundColor(.accentColor)
        }.padding(.horizontal).padding(.vertical, 5)
    }
}

struct RangeSlider: View {
    @Binding var minValue: Double
    @Binding var maxValue: Double
    
    let range: ClosedRange<Double>
    
    var body: some View {
        GeometryReader { geometry in
            let totalWidth = geometry.size.width
            let minPos = (self.minValue - self.range.lowerBound) / (self.range.upperBound - self.range.lowerBound) * totalWidth
            let maxPos = (self.maxValue - self.range.lowerBound) / (self.range.upperBound - self.range.lowerBound) * totalWidth

            ZStack(alignment: .leading) {
                RoundedRectangle(cornerRadius: 2).fill(Color.secondary.opacity(0.3)).frame(height: 4)
                RoundedRectangle(cornerRadius: 2).fill(Color.accentColor).frame(width: maxPos - minPos, height: 4).offset(x: minPos)
                
                Thumb(value: self.$minValue, range: self.range, totalWidth: totalWidth, otherValue: self.$maxValue, isMin: true).offset(x: minPos - 8)
                Thumb(value: self.$maxValue, range: self.range, totalWidth: totalWidth, otherValue: self.$minValue, isMin: false).offset(x: maxPos - 8)
            }
        }
        .frame(height: 20)
    }
    
    struct Thumb: View {
        @Binding var value: Double
        let range: ClosedRange<Double>
        let totalWidth: CGFloat
        @Binding var otherValue: Double
        let isMin: Bool
        
        @State private var isDragging = false

        var body: some View {
            Circle().fill(Color.accentColor).frame(width: 16, height: 16)
                .overlay(Circle().stroke(Color.primary.opacity(0.2), lineWidth: 1))
                .shadow(radius: isDragging ? 4 : 2)
                .scaleEffect(isDragging ? 1.1 : 1.0)
                .animation(.interactiveSpring(response: 0.3, dampingFraction: 0.8), value: isDragging)
                .gesture(
                    DragGesture(minimumDistance: 0)
                        .onChanged { gesture in
                            if !isDragging { isDragging = true }
                            let currentPos = (self.value - range.lowerBound) / (range.upperBound - range.lowerBound) * totalWidth
                            let newPosition = currentPos + gesture.translation.width
                            let clampedPosition = max(0, min(totalWidth, newPosition))
                            let newValue = (clampedPosition / totalWidth) * (range.upperBound - range.lowerBound) + range.lowerBound
                            if isMin { self.value = min(newValue, otherValue) }
                            else { self.value = max(newValue, otherValue) }
                        }
                        .onEnded { _ in isDragging = false }
                )
        }
    }
}


extension Color {
    var highContrast: Color {
        let platformColor = NSColor(self)
        guard let rgbColor = platformColor.usingColorSpace(.sRGB) else {
            return .primary
            
        }
        
        var r: CGFloat = 0, g: CGFloat = 0, b: CGFloat = 0
        rgbColor.getRed(&r, green: &g, blue: &b, alpha: nil)
        
        
        let luminance = (0.299 * r) + (0.587 * g) + (0.114 * b)
        
        
        return luminance > 0.6 ? .black : .white
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View { ContentView() }
}
