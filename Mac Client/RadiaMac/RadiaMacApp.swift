//
//  RadiaMacApp.swift
//  RadiaMac
//
//  Created by William Sharp on 2/9/26.
//

import SwiftUI

@main
struct RadiaMacApp: App {
    @StateObject private var socketData = SocketManager()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(socketData)
        }

        Window("Live Spectrogram", id: "spectrogramWindow") {
            PopOutSpectrogramView().environmentObject(socketData)
        }
        
        Window("CPS Graph", id: "cpsWindow") {
            PopOutCpsView().environmentObject(socketData)
        }
        
        Window("Dosage Graph", id: "dosageWindow") {
            PopOutDosageView().environmentObject(socketData)
        }
        
        Window("Live Spectrum", id: "spectrumWindow") {
            PopOutSpectrumView().environmentObject(socketData)
        }
    }
}
