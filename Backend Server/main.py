from radiacode import RadiaCode, RealTimeData
from dataclasses import dataclass
from typing import Dict, List
import json

from gamma_emissions_library import CreateSearch

import numpy as np
from scipy.signal import find_peaks

import asyncio
import websockets

probeDevice = RadiaCode()

#I need to remind myself: pyinstaller --onedir --noconsole main.py

cpsDict: List = []
dosageDict: List = []

async def looper(websocket):
    while True:
        currentSpectrum = probeDevice.spectrum()
        spectrumCounts: List[int] = currentSpectrum.counts

        spectrumDict: List = []
        # a0+a1⋅ch+a2⋅ch

        peaksDict: List = []

        for index, value in enumerate(spectrumCounts):
            toAppend = {
                "counts": value,
                "energy": (currentSpectrum.a0 + currentSpectrum.a1 * index + currentSpectrum.a2 * index)
            }
            spectrumDict.append(toAppend)


        peaks, properties = find_peaks(np.array(spectrumCounts), prominence=15, width=5, height=10)
        
        for peak in peaks.tolist():
            isotopeNamesList = []
            itemEnergy = spectrumDict[peak]["energy"]

            for i in CreateSearch().Search.InRange(itemEnergy, 1):
                isotopeNamesList.append(i.Name)

            appendItem = {
                "energy": itemEnergy,
                "counts": spectrumDict[peak]["counts"],
                "isotopeNames": isotopeNamesList
            }
            peaksDict.append(appendItem)

        for record in probeDevice.data_buf():
            if isinstance(record, RealTimeData):
                currentSecond = currentSpectrum.duration.total_seconds()
                appendCPS = {
                    "time": currentSecond,
                    "cps": record.count_rate
                }
                appendDosage = {
                    "time": currentSecond,
                    "dosage": (record.dose_rate*10000)
                }
                cpsDict.append(appendCPS)
                dosageDict.append(appendDosage)

        

        DictReturn: Dict = {
            "spectrumData": {
                "spectrum": spectrumDict,
                "a0": currentSpectrum.a0,
                "a1": currentSpectrum.a1,
                "a2": currentSpectrum.a2,
                "duration": currentSpectrum.duration.total_seconds(),
                "peaks": peaksDict
            },
            "deviceValue": {
                "dosage": dosageDict,
                "countRate": cpsDict,
                "serialNumber": probeDevice.serial_number()
            },
        }
        await websocket.send(json.dumps(DictReturn))
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(looper, "localhost", 8945):
        await asyncio.Future()

asyncio.run(main())