//
//  WindowDelegate.swift
//  RadiaMac
//
//  Created by William Sharp on 8/13/25.
//
import Cocoa

class WindowDelegate: NSObject, NSWindowDelegate {
    
    func windowShouldClose(_ sender: NSWindow) -> Bool {
        let alert = NSAlert()
        alert.messageText = "Quit the Application?"
        alert.informativeText = "Are you sure you want to quit? All unsaved changes will be lost."
        alert.alertStyle = .warning
        
        
        alert.addButton(withTitle: "Quit")
        alert.addButton(withTitle: "Cancel")

        
        let response = alert.runModal()

        
        if response == .alertFirstButtonReturn {

            return true
        } else {
            return false
        }
    }
}
