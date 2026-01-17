// PythonServerManager.swift
// RadiaMac App
import Foundation
import AppKit

@MainActor
final class PythonServerManager: ObservableObject {
    
    private var serverProcess: Process?
    
    init() {
        NotificationCenter.default.addObserver(self, selector: #selector(stopServer), name: NSApplication.willTerminateNotification, object: nil)
    }
    
    func startServer(settings: LaunchSettings) {
        guard serverProcess == nil else { return }
        guard let path = Bundle.main.path(forResource: "Server_Script", ofType: nil) else {
            print("FATAL ERROR: Could not find 'Server_Script' in the app bundle.")
            return
        }
        
        print("Starting Python server...")
        
        
        var arguments: [String] = [
            "--device-serial", settings.deviceSerial,
            "--measurement-seconds", String(settings.measurementSeconds)
        ]
        
        
        if !settings.resetSpectrumOnLaunch {
            arguments.append("--no-reset")
        }
        
        
        if settings.resetDoseOnLaunch {
            arguments.append("--reset-dose")
        }
        
        serverProcess = Process()
        serverProcess?.executableURL = URL(fileURLWithPath: path)
        serverProcess?.arguments = arguments
        serverProcess?.environment = ["PATH": "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"]
        
        let outputPipe = Pipe()
        serverProcess?.standardOutput = outputPipe
        outputPipe.fileHandleForReading.readabilityHandler = { handle in
            if let line = String(data: handle.availableData, encoding: .utf8), !line.isEmpty {
                print("[PyServer]: \(line.trimmingCharacters(in: .whitespacesAndNewlines))")
            }
        }
        
        do {
            try serverProcess?.run()
            print("Server process started successfully with PID: \(serverProcess?.processIdentifier ?? -1)")
        } catch {
            print("Failed to run server process: \(error)")
            serverProcess = nil
        }
    }
    
    @objc func stopServer() {
        guard let serverProcess = serverProcess, serverProcess.isRunning else { return }
        print("Stopping server (PID: \(serverProcess.processIdentifier))...")
        serverProcess.terminate()
        self.serverProcess = nil
    }
}
