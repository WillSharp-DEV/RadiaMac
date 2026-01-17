// LaunchSettings.swift
// RadiaMac App
import SwiftUI

final class LaunchSettings: ObservableObject {
    @AppStorage("deviceSerial") var deviceSerial: String = "RC-110-001492"
    @AppStorage("measurementSeconds") var measurementSeconds: Int = 1
    @AppStorage("resetSpectrum") var resetSpectrumOnLaunch: Bool = true
    @AppStorage("resetDose") var resetDoseOnLaunch: Bool = true // ADDED
    func resetToDefaults() {
        let currentSerial = deviceSerial
        
        measurementSeconds = 1
        resetSpectrumOnLaunch = true
        resetDoseOnLaunch = true // ADDED
        
        deviceSerial = currentSerial
    }

    func validateSettings() {
        measurementSeconds = max(1, min(60, measurementSeconds))
    }
}
