//
//  RadiaMacApp.swift
//  RadiaMac
//
//  Created by William Sharp on 2/9/26.
//

import SwiftUI
import SwiftData

@main

class AppDelegate: NSObject, NSApplicationDelegate {
    
    let serverManager = ServerManager()

    func applicationDidFinishLaunching(_ notification: Notification) {
        
        serverManager.startServer()
    }

    func applicationWillTerminate(_ notification: Notification) {
        serverManager.stopServer()
    }
}

struct RadiaMacApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    var sharedModelContainer: ModelContainer = {
        let schema = Schema([
            Item.self,
        ])
        let modelConfiguration = ModelConfiguration(schema: schema, isStoredInMemoryOnly: false)

        do {
            return try ModelContainer(for: schema, configurations: [modelConfiguration])
        } catch {
            fatalError("Could not create ModelContainer: \(error)")
        }
    }()

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(sharedModelContainer)
    }
}
