// ConfigurationView.swift
// RadiaMac App
//
// This SwiftUI View creates the user interface for changing the settings.

import SwiftUI

struct ConfigurationView: View {
    @ObservedObject var settings: LaunchSettings
    var onLaunch: () -> Void
    
    @State private var showingHelp: String? = nil
    
    var body: some View {
        Form {
            Section(header: Text("Device & Measurement")) {
                HStack {
                    TextField("Device Serial", text: $settings.deviceSerial)
                    HelpButton(id: "serial", showingHelp: $showingHelp)
                }
                HStack {
                    Stepper("Measurement Interval (s): \(settings.measurementSeconds)", value: $settings.measurementSeconds, in: 1...60)
                    HelpButton(id: "interval", showingHelp: $showingHelp)
                }
                HStack {
                    Toggle("Reset Spectrum on Launch", isOn: $settings.resetSpectrumOnLaunch)
                    HelpButton(id: "resetSpectrum", showingHelp: $showingHelp)
                }
                
                HStack {
                    Toggle("Reset Accumulated Dose on Launch", isOn: $settings.resetDoseOnLaunch)
                    HelpButton(id: "resetDose", showingHelp: $showingHelp)
                }
            }
            
            
            
            HStack {
                Button(action: settings.resetToDefaults) {
                    Label("Reset to Defaults", systemImage: "arrow.counterclockwise").frame(maxWidth: .infinity)
                }
                .buttonStyle(.bordered)
                
                Button(action: onLaunch) {
                    Text("Launch Server & Start App").frame(maxWidth: .infinity)
                }
                .buttonStyle(.borderedProminent)
            }
            .padding(.top)
        }
        .padding()
        .frame(width: 520)
        .fixedSize()
        .popover(item: Binding<HelpItem?>(
            get: { showingHelp.map { HelpItem(id: $0) } },
            set: { showingHelp = $0?.id }
        )) { item in
            HelpPopover(helpId: item.id).frame(width: 350)
        }
    }
}


struct HelpPopover: View {
    let helpId: String
    
    var helpContent: (title: String, description: String) {
        switch helpId {
        case "serial": return ("Device Serial", "The unique identifier of your radiation detector.")
        case "interval": return ("Measurement Interval", "How often (in seconds) to acquire new data. Recommended: 1-5 seconds.")
        case "resetSpectrum": return ("Reset Spectrum", "If enabled, the device's accumulated spectrum will be cleared on launch. Disable to continue a previous measurement.")
        
        case "resetDose": return ("Reset Accumulated Dose", "If enabled, the saved total accumulated dose will be cleared on launch. Disable to continue accumulating dose across sessions.")
        
        default: return ("Help", "No help available for this item.")
        }
    }
    
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            Text(helpContent.title).font(.headline)
            Text(helpContent.description).font(.caption).fixedSize(horizontal: false, vertical: true)
            Text("Press ESC to close").font(.caption2).foregroundColor(.secondary)
        }
        .padding()
    }
}


struct HelpButton: View {
    let id: String
    @Binding var showingHelp: String?
    var body: some View {
        Button(action: { showingHelp = id }) {
            Image(systemName: "questionmark.circle").foregroundColor(.secondary)
        }
        .buttonStyle(.plain)
    }
}

struct HelpItem: Identifiable { let id: String }
