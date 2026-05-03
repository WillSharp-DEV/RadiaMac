import json
from typing import Any
from typing import List
from dataclasses import dataclass
import re


GlobalLibrary = [
    {
        "E(keV)": 186.21,
        "Intensity": 3.59,
        "Nuclide": "Ra-226",
        "Half_Life": "1600 Y",
        "Natural": True
    },
    {
        "E(keV)": 238.63,
        "Intensity": 43.6,
        "Nuclide": "Pb-212",
        "Half_Life": "10.64 H",
        "Natural": True
    },
    {
        "E(keV)": 241.99,
        "Intensity": 7.25,
        "Nuclide": "Pb-214",
        "Half_Life": "26.8 M",
        "Natural": True
    },
    {
        "E(keV)": 279.19,
        "Intensity": 6.0,
        "Nuclide": "Hg-203",
        "Half_Life": "46.6 D",
        "Natural": False
    },
    {
        "E(keV)": 295.22,
        "Intensity": 18.4,
        "Nuclide": "Pb-214",
        "Half_Life": "26.8 M",
        "Natural": True
    },
    {
        "E(keV)": 300.09,
        "Intensity": 3.11,
        "Nuclide": "Pa-231",
        "Half_Life": "3.28E4 Y",
        "Natural": True
    },
    {
        "E(keV)": 320.08,
        "Intensity": 9.91,
        "Nuclide": "Cr-51",
        "Half_Life": "27.7 D",
        "Natural": False
    },
    {
        "E(keV)": 328.76,
        "Intensity": 20.7,
        "Nuclide": "La-140",
        "Half_Life": "1.678 D",
        "Natural": False
    },
    {
        "E(keV)": 338.32,
        "Intensity": 11.3,
        "Nuclide": "Ac-228",
        "Half_Life": "6.15 H",
        "Natural": True
    },
    {
        "E(keV)": 344.28,
        "Intensity": 26.6,
        "Nuclide": "Eu-152",
        "Half_Life": "13.52 Y",
        "Natural": False
    },
    {
        "E(keV)": 351.93,
        "Intensity": 35.6,
        "Nuclide": "Pb-214",
        "Half_Life": "26.8 M",
        "Natural": True
    },
    {
        "E(keV)": 356.01,
        "Intensity": 62.05,
        "Nuclide": "Ba-133",
        "Half_Life": "10.51 Y",
        "Natural": False
    },
    {
        "E(keV)": 364.49,
        "Intensity": 81.5,
        "Nuclide": "I-131",
        "Half_Life": "8.02 D",
        "Natural": False
    },
    {
        "E(keV)": 414.7,
        "Intensity": 29.8,
        "Nuclide": "Pu-239",
        "Half_Life": "2.41E4 Y",
        "Natural": False
    },
    {
        "E(keV)": 427.87,
        "Intensity": 29.6,
        "Nuclide": "Sb-125",
        "Half_Life": "2.76 Y",
        "Natural": False
    },
    {
        "E(keV)": 443.96,
        "Intensity": 3.12,
        "Nuclide": "Eu-152",
        "Half_Life": "13.52 Y",
        "Natural": False
    },
    {
        "E(keV)": 463.0,
        "Intensity": 4.4,
        "Nuclide": "Ac-228",
        "Half_Life": "6.15 H",
        "Natural": True
    },
    {
        "E(keV)": 477.6,
        "Intensity": 10.3,
        "Nuclide": "Be-7",
        "Half_Life": "53.22 D",
        "Natural": True
    },
    {
        "E(keV)": 487.02,
        "Intensity": 45.5,
        "Nuclide": "La-140",
        "Half_Life": "1.678 D",
        "Natural": False
    },
    {
        "E(keV)": 497.08,
        "Intensity": 91.0,
        "Nuclide": "Ru-103",
        "Half_Life": "39.26 D",
        "Natural": False
    },
    {
        "E(keV)": 511.0,
        "Intensity": 180.0,
        "Nuclide": "Annihilation (Na-22/Positron)",
        "Half_Life": "N/A",
        "Natural": False
    },
    {
        "E(keV)": 514.0,
        "Intensity": 15.1,
        "Nuclide": "Kr-85",
        "Half_Life": "10.76 Y",
        "Natural": False
    },
    {
        "E(keV)": 563.2,
        "Intensity": 2.65,
        "Nuclide": "Cs-134",
        "Half_Life": "2.065 Y",
        "Natural": False
    },
    {
        "E(keV)": 569.7,
        "Intensity": 15.4,
        "Nuclide": "Cs-134",
        "Half_Life": "2.065 Y",
        "Natural": False
    },
    {
        "E(keV)": 583.19,
        "Intensity": 85.0,
        "Nuclide": "Tl-208",
        "Half_Life": "3.053 M",
        "Natural": True
    },
    {
        "E(keV)": 600.6,
        "Intensity": 17.6,
        "Nuclide": "Sb-125",
        "Half_Life": "2.76 Y",
        "Natural": False
    },
    {
        "E(keV)": 604.72,
        "Intensity": 97.6,
        "Nuclide": "Cs-134",
        "Half_Life": "2.065 Y",
        "Natural": False
    },
    {
        "E(keV)": 609.31,
        "Intensity": 45.5,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 621.93,
        "Intensity": 9.93,
        "Nuclide": "Rh-106",
        "Half_Life": "29.8 S",
        "Natural": False
    },
    {
        "E(keV)": 635.95,
        "Intensity": 11.2,
        "Nuclide": "Sb-125",
        "Half_Life": "2.76 Y",
        "Natural": False
    },
    {
        "E(keV)": 661.66,
        "Intensity": 85.1,
        "Nuclide": "Cs-137",
        "Half_Life": "30.17 Y",
        "Natural": False
    },
    {
        "E(keV)": 662.4,
        "Intensity": 94.6,
        "Nuclide": "Ag-110m",
        "Half_Life": "249.76 D",
        "Natural": False
    },
    {
        "E(keV)": 696.5,
        "Intensity": 1.34,
        "Nuclide": "Pr-144",
        "Half_Life": "17.28 M",
        "Natural": False
    },
    {
        "E(keV)": 722.9,
        "Intensity": 90.8,
        "Nuclide": "I-131",
        "Half_Life": "8.02 D",
        "Natural": False
    },
    {
        "E(keV)": 724.19,
        "Intensity": 44.3,
        "Nuclide": "Zr-95",
        "Half_Life": "64.0 D",
        "Natural": False
    },
    {
        "E(keV)": 727.3,
        "Intensity": 6.7,
        "Nuclide": "Bi-212",
        "Half_Life": "60.55 M",
        "Natural": True
    },
    {
        "E(keV)": 756.73,
        "Intensity": 54.5,
        "Nuclide": "Zr-95",
        "Half_Life": "64.0 D",
        "Natural": False
    },
    {
        "E(keV)": 765.8,
        "Intensity": 99.8,
        "Nuclide": "Nb-95",
        "Half_Life": "34.99 D",
        "Natural": False
    },
    {
        "E(keV)": 778.9,
        "Intensity": 12.9,
        "Nuclide": "Eu-152",
        "Half_Life": "13.52 Y",
        "Natural": False
    },
    {
        "E(keV)": 795.6,
        "Intensity": 85.4,
        "Nuclide": "Cs-134",
        "Half_Life": "2.065 Y",
        "Natural": False
    },
    {
        "E(keV)": 795.9,
        "Intensity": 4.66,
        "Nuclide": "Ac-228",
        "Half_Life": "6.15 H",
        "Natural": True
    },
    {
        "E(keV)": 801.9,
        "Intensity": 8.7,
        "Nuclide": "Cs-134",
        "Half_Life": "2.065 Y",
        "Natural": False
    },
    {
        "E(keV)": 815.77,
        "Intensity": 23.3,
        "Nuclide": "La-140",
        "Half_Life": "1.678 D",
        "Natural": False
    },
    {
        "E(keV)": 834.85,
        "Intensity": 99.98,
        "Nuclide": "Mn-54",
        "Half_Life": "312.3 D",
        "Natural": False
    },
    {
        "E(keV)": 860.56,
        "Intensity": 12.5,
        "Nuclide": "Tl-208",
        "Half_Life": "3.053 M",
        "Natural": True
    },
    {
        "E(keV)": 867.38,
        "Intensity": 4.26,
        "Nuclide": "Eu-152",
        "Half_Life": "13.52 Y",
        "Natural": False
    },
    {
        "E(keV)": 871.1,
        "Intensity": 3.4,
        "Nuclide": "O-15 (Water Activation)",
        "Half_Life": "122 S",
        "Natural": False
    },
    {
        "E(keV)": 884.5,
        "Intensity": 72.7,
        "Nuclide": "Ag-110m",
        "Half_Life": "249.76 D",
        "Natural": False
    },
    {
        "E(keV)": 898.04,
        "Intensity": 93.9,
        "Nuclide": "Y-88",
        "Half_Life": "106.65 D",
        "Natural": False
    },
    {
        "E(keV)": 911.2,
        "Intensity": 25.8,
        "Nuclide": "Ac-228",
        "Half_Life": "6.15 H",
        "Natural": True
    },
    {
        "E(keV)": 934.0,
        "Intensity": 3.1,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 937.4,
        "Intensity": 34.4,
        "Nuclide": "Ag-110m",
        "Half_Life": "249.76 D",
        "Natural": False
    },
    {
        "E(keV)": 954.55,
        "Intensity": 18.2,
        "Nuclide": "Mn-52",
        "Half_Life": "5.59 D",
        "Natural": False
    },
    {
        "E(keV)": 964.08,
        "Intensity": 14.6,
        "Nuclide": "Eu-152",
        "Half_Life": "13.52 Y",
        "Natural": False
    },
    {
        "E(keV)": 968.97,
        "Intensity": 15.8,
        "Nuclide": "Ac-228",
        "Half_Life": "6.15 H",
        "Natural": True
    },
    {
        "E(keV)": 1001.03,
        "Intensity": 0.84,
        "Nuclide": "Pa-234m",
        "Half_Life": "1.17 M",
        "Natural": True
    },
    {
        "E(keV)": 1050.4,
        "Intensity": 1.5,
        "Nuclide": "Rh-106",
        "Half_Life": "29.8 S",
        "Natural": False
    },
    {
        "E(keV)": 1063.66,
        "Intensity": 22.7,
        "Nuclide": "Bi-207",
        "Half_Life": "31.55 Y",
        "Natural": False
    },
    {
        "E(keV)": 1077.3,
        "Intensity": 2.74,
        "Nuclide": "Rb-86",
        "Half_Life": "18.6 D",
        "Natural": False
    },
    {
        "E(keV)": 1085.9,
        "Intensity": 10.2,
        "Nuclide": "Eu-152",
        "Half_Life": "13.52 Y",
        "Natural": False
    },
    {
        "E(keV)": 1112.1,
        "Intensity": 13.6,
        "Nuclide": "Eu-152",
        "Half_Life": "13.52 Y",
        "Natural": False
    },
    {
        "E(keV)": 1115.54,
        "Intensity": 50.6,
        "Nuclide": "Zn-65",
        "Half_Life": "244.3 D",
        "Natural": False
    },
    {
        "E(keV)": 1120.29,
        "Intensity": 14.9,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 1157.0,
        "Intensity": 1.63,
        "Nuclide": "Sc-44",
        "Half_Life": "3.97 H",
        "Natural": False
    },
    {
        "E(keV)": 1167.97,
        "Intensity": 1.8,
        "Nuclide": "Cs-134",
        "Half_Life": "2.065 Y",
        "Natural": False
    },
    {
        "E(keV)": 1173.23,
        "Intensity": 99.9,
        "Nuclide": "Co-60",
        "Half_Life": "5.27 Y",
        "Natural": False
    },
    {
        "E(keV)": 1238.12,
        "Intensity": 5.8,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 1274.53,
        "Intensity": 99.9,
        "Nuclide": "Na-22",
        "Half_Life": "2.60 Y",
        "Natural": False
    },
    {
        "E(keV)": 1291.6,
        "Intensity": 41.0,
        "Nuclide": "Fe-59",
        "Half_Life": "44.5 D",
        "Natural": False
    },
    {
        "E(keV)": 1293.56,
        "Intensity": 14.3,
        "Nuclide": "Ar-41",
        "Half_Life": "1.83 H",
        "Natural": False
    },
    {
        "E(keV)": 1299.1,
        "Intensity": 1.63,
        "Nuclide": "Eu-152",
        "Half_Life": "13.52 Y",
        "Natural": False
    },
    {
        "E(keV)": 1332.5,
        "Intensity": 99.98,
        "Nuclide": "Co-60",
        "Half_Life": "5.27 Y",
        "Natural": False
    },
    {
        "E(keV)": 1368.6,
        "Intensity": 100.0,
        "Nuclide": "Na-24",
        "Half_Life": "15.0 H",
        "Natural": False
    },
    {
        "E(keV)": 1377.67,
        "Intensity": 3.9,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 1383.93,
        "Intensity": 66.6,
        "Nuclide": "Ag-110m",
        "Half_Life": "249.76 D",
        "Natural": False
    },
    {
        "E(keV)": 1401.5,
        "Intensity": 1.3,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 1408.01,
        "Intensity": 20.8,
        "Nuclide": "Eu-152",
        "Half_Life": "13.52 Y",
        "Natural": False
    },
    {
        "E(keV)": 1434.7,
        "Intensity": 100.0,
        "Nuclide": "Mn-52",
        "Half_Life": "5.59 D",
        "Natural": False
    },
    {
        "E(keV)": 1459.1,
        "Intensity": 0.84,
        "Nuclide": "Ac-228",
        "Half_Life": "6.15 H",
        "Natural": True
    },
    {
        "E(keV)": 1460.82,
        "Intensity": 10.66,
        "Nuclide": "K-40",
        "Half_Life": "1.25E9 Y",
        "Natural": True
    },
    {
        "E(keV)": 1489.1,
        "Intensity": 0.28,
        "Nuclide": "Pr-144",
        "Half_Life": "17.28 M",
        "Natural": False
    },
    {
        "E(keV)": 1505.0,
        "Intensity": 29.8,
        "Nuclide": "Ag-110m",
        "Half_Life": "249.76 D",
        "Natural": False
    },
    {
        "E(keV)": 1509.2,
        "Intensity": 2.1,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 1567.8,
        "Intensity": 1.3,
        "Nuclide": "Cs-134",
        "Half_Life": "2.065 Y",
        "Natural": False
    },
    {
        "E(keV)": 1588.2,
        "Intensity": 3.2,
        "Nuclide": "Ac-228",
        "Half_Life": "6.15 H",
        "Natural": True
    },
    {
        "E(keV)": 1596.21,
        "Intensity": 95.4,
        "Nuclide": "La-140",
        "Half_Life": "1.678 D",
        "Natural": False
    },
    {
        "E(keV)": 1620.5,
        "Intensity": 1.5,
        "Nuclide": "Bi-212",
        "Half_Life": "60.55 M",
        "Natural": True
    },
    {
        "E(keV)": 1630.6,
        "Intensity": 1.5,
        "Nuclide": "Ac-228",
        "Half_Life": "6.15 H",
        "Natural": True
    },
    {
        "E(keV)": 1661.2,
        "Intensity": 1.05,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 1729.59,
        "Intensity": 2.8,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 1764.49,
        "Intensity": 15.3,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 1770.2,
        "Intensity": 71.64,
        "Nuclide": "Bi-207",
        "Half_Life": "31.55 Y",
        "Natural": False
    },
    {
        "E(keV)": 1836.06,
        "Intensity": 99.2,
        "Nuclide": "Y-88",
        "Half_Life": "106.65 D",
        "Natural": False
    },
    {
        "E(keV)": 1847.4,
        "Intensity": 2.0,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 2118.5,
        "Intensity": 1.1,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 2185.7,
        "Intensity": 0.7,
        "Nuclide": "Pr-144",
        "Half_Life": "17.28 M",
        "Natural": False
    },
    {
        "E(keV)": 2204.2,
        "Intensity": 4.9,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 2447.7,
        "Intensity": 1.5,
        "Nuclide": "Bi-214",
        "Half_Life": "19.9 M",
        "Natural": True
    },
    {
        "E(keV)": 2614.51,
        "Intensity": 99.75,
        "Nuclide": "Tl-208",
        "Half_Life": "3.053 M",
        "Natural": True
    },
    {
        "E(keV)": 2754.0,
        "Intensity": 99.85,
        "Nuclide": "Na-24",
        "Half_Life": "15.0 H",
        "Natural": False
    }
]

@dataclass
class ReturnItem:
    Name: str
    Intensity: float
    Energy: float


class SearchConstructor:
    def __init__(self):
        return
    def InRange(self, Energy: float, LeftRightRange: float, naturalFilter: bool = True) -> List[ReturnItem]:
        ReturnList: List[ReturnItem] = []
        LeftVal: float = (Energy - (LeftRightRange/2))
        RightVal: float = (Energy + (LeftRightRange/2))
        for i in GlobalLibrary:
            if i["E(keV)"] >= LeftVal and i["E(keV)"] <= RightVal and i["Natural"] == naturalFilter:
                Item = ReturnItem(i['Nuclide'], i['Intensity'], i["E(keV)"])
                ReturnList.append(Item)
        return ReturnList



class CreateSearch:
    def __init__(self):
        self.Search = SearchConstructor()
        return