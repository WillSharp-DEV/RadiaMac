// RadiaMacApp.swift

import SwiftUI

@main
struct RadiaMacApp: App {
    
    
    @StateObject private var launchSettings = LaunchSettings()
    
    
    @NSApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    
    
    @State private var isServerLaunched = false

    var body: some Scene {
        WindowGroup {
            if isServerLaunched {
                
                ContentView()
            } else {
                
                
                ConfigurationView(settings: launchSettings) {
                    
                    
                    appDelegate.pythonServerManager.startServer(settings: launchSettings)
                    
                    
                    isServerLaunched = true
                }
            }
        }
        
        .environmentObject(appDelegate.pythonServerManager)
    }
}
