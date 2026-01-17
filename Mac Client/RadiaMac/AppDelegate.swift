import Cocoa
import SwiftUI


@MainActor
class AppDelegate: NSObject, NSApplicationDelegate {

    
    let pythonServerManager = PythonServerManager()

    func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply {
        let alert = NSAlert()
        alert.messageText = "Quit Application?"
        alert.informativeText = "Are you sure you want to quit? This will stop the server."
        alert.alertStyle = .warning

        alert.addButton(withTitle: "Quit")
        alert.addButton(withTitle: "Cancel")
        
        let response = alert.runModal()

        if response == .alertFirstButtonReturn {
            
            
            
            print("App is terminating, stopping Python server...")
            self.pythonServerManager.stopServer()
            
            
            return .terminateNow
        } else {
            
            return .terminateCancel
        }
    }
}
