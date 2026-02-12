//
//  ContentView.swift
//  RadiaMac
//
//  Created by William Sharp on 2/9/26.
//

import SwiftUI
import SwiftData
import Starscream
import Charts
import SwiftyJSON
internal import System
internal import Combine

struct SpectrumGraph: Identifiable, Codable {
    var id: Double { energy }
    
    let counts: Double
    let energy: Double
    
    enum CodingKeys: String, CodingKey {
        case counts
        case energy
    }
}

struct CpsGraph: Identifiable, Codable {
    var id: Double { time }
    
    let time: Double
    let cps: Double
    
    enum CodingKeys: String, CodingKey {
        case time
        case cps
    }
}

struct DosageGraph: Identifiable, Codable {
    var id: Double { time }
    
    let time: Double
    let dosage: Double
    
    enum CodingKeys: String, CodingKey {
        case time
        case dosage
    }
}

struct PeakInfo: Identifiable, Codable {
    var id: Double { energy }
    
    let energy: Double
    let counts: Double
    let isotopeNames: [String]
    
    enum CodingKeys: String, CodingKey {
        case energy
        case counts
        case isotopeNames
    }
}

struct DeviceValues: Codable {
    let dosage: [DosageGraph]
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
}

class SocketManager: ObservableObject, WebSocketDelegate {
    
    @Published var liveData = DataReturnCodable(
        spectrumData: SpectrumItem(
            spectrum: [SpectrumGraph(counts: 0, energy: 0)],
            a0: 0,
            a1: 0,
            a2: 0,
            duration: 0,
            peaks: []
        ),
        deviceValue: DeviceValues(
            dosage: [],
            countRate: [],
            serialNumber: "Waiting..."
        )
    )
    
    var webSocket: WebSocket?
    
    func getData() {
        var request = URLRequest(url: URL(string: "ws://localhost:8945")!)
        request.timeoutInterval = 1
        
        webSocket = WebSocket(request: request)
        webSocket?.delegate = self
        webSocket?.connect()
    }
    
    func didReceive(event: WebSocketEvent, client: any WebSocketClient) {
        switch event {
        case .connected(let headers):
            print("CONNECTED TO SOCKET")
        case .text(let string):
            if let data = string.data(using: .utf8) {
                do {
                    let decoder = JSONDecoder()
                    let toReturn = try decoder .decode(DataReturnCodable.self, from: data)
                    DispatchQueue.main.async {
                        self.liveData = toReturn
                        
                    }
                } catch {
                    print("ERROR WITH SPECTRUM CODABLE")
                }
            }
        default:
            break
        }
    }
    
}


struct ContentView: View {
    @StateObject var SpectrumData = SocketManager()
    var body: some View {
        VStack {
            HStack {
                VStack {
                    Text("Dosage: \(String(SpectrumData.liveData.deviceValue.dosage.last?.dosage ?? 0))")
                    Text("cps: \(String(SpectrumData.liveData.deviceValue.countRate.last?.cps ?? 0))")
                    Text("CPS graph")
                    Chart {
                        ForEach(SpectrumData.liveData.deviceValue.countRate) { index in
                            LineMark(
                                x: .value("Time (seconds)", index.time),
                                y: .value("cps", index.cps)
                            )
                            
                        }
                    }.chartXScale(domain: (SpectrumData.liveData.deviceValue.countRate.first?.time ?? 0) ... (SpectrumData.liveData.deviceValue.countRate.last?.time ?? 10))
                    Text("Dosage graph")
                    Chart {
                        ForEach(SpectrumData.liveData.deviceValue.dosage) { index in
                            LineMark(
                                x: .value("Time (seconds)", index.time),
                                y: .value("Dosage", index.dosage)
                            )
                            
                        }
                    }.chartXScale(domain: (SpectrumData.liveData.deviceValue.dosage.first?.time ?? 0) ... (SpectrumData.liveData.deviceValue.dosage.last?.time ?? 10))
                    Text("Peak information")
                    List {
                        ForEach(SpectrumData.liveData.spectrumData.peaks.indices, id: \.self) { index in
                            Text("[\(index)]: \(SpectrumData.liveData.spectrumData.peaks[index].isotopeNames.joined(separator: ", "))")
                        }
                    }
                }
                VStack {
                    Chart {
                        ForEach(SpectrumData.liveData.spectrumData.spectrum) { index in
                            LineMark(
                                x: .value("Energy", index.energy),
                                y: .value("Counts", index.counts)
                            )
                            
                        }
                        ForEach(SpectrumData.liveData.spectrumData.peaks.indices, id:\.self) { index in
                            PointMark(
                                x: .value("Energy", SpectrumData.liveData.spectrumData.peaks[index].energy),
                                y: .value("counts", SpectrumData.liveData.spectrumData.peaks[index].counts)
                            ).foregroundStyle(.green).annotation(position: .top) {
                                Text(String(index))
                        }
                        }
                    }.chartXScale(domain: 0...2450)
                }
            }
        }.padding(10).onAppear() {
            SpectrumData.getData()
        }
    }

}

#Preview {
    ContentView()
        .modelContainer(for: Item.self, inMemory: true)
}
