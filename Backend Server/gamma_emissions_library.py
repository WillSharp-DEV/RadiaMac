import json
from typing import Any
from typing import List
from dataclasses import dataclass
import re


@dataclass
class ReturnItem:
    Name: str
    Intensity: float
    Energy: float



GlobalLibrary = [
    {
        "E(keV)": 6.24,
        "Intensity": 1.031,
        "Nuclide": "W-181 (EC 121.2 D)"
    },
    {
        "E(keV)": 6.3,
        "Intensity": 0.01151,
        "Nuclide": "Hf-181 (B- 42.39 D)"
    },
    {
        "E(keV)": 7.133,
        "Intensity": 4.95,
        "Nuclide": "Er-160 (EC 28.58 H)"
    },
    {
        "E(keV)": 8.41031,
        "Intensity": 0.331,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 8.41031,
        "Intensity": 0.158,
        "Nuclide": "Er-169 (B- 9.40 D)"
    },
    {
        "E(keV)": 10.49,
        "Intensity": 0.004881,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 12.327,
        "Intensity": 1.531,
        "Nuclide": "Ba-133m (IT 38.9 H)"
    },
    {
        "E(keV)": 12.47,
        "Intensity": 3e-06,
        "Nuclide": "Ca-45 (B- 162.61 D)"
    },
    {
        "E(keV)": 12.7,
        "Intensity": 0.009824,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 12.75,
        "Intensity": 0.304,
        "Nuclide": "Ra-228 (B- 5.75 Y)"
    },
    {
        "E(keV)": 13.263,
        "Intensity": 0.089,
        "Nuclide": "As-73 (EC 80.30 D)"
    },
    {
        "E(keV)": 13.4,
        "Intensity": 0.000159,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 13.52,
        "Intensity": 1.6,
        "Nuclide": "Ra-228 (B- 5.75 Y)"
    },
    {
        "E(keV)": 13.8,
        "Intensity": 0.01965,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 13.81,
        "Intensity": 0.099,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 13.846,
        "Intensity": 1.22,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 13.9,
        "Intensity": 0.032,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 14.06383,
        "Intensity": 0.0178,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 14.4129,
        "Intensity": 9.158,
        "Nuclide": "Co-57 (EC 271.74 D)"
    },
    {
        "E(keV)": 15.5,
        "Intensity": 0.16,
        "Nuclide": "Ra-228 (B- 5.75 Y)"
    },
    {
        "E(keV)": 16.2,
        "Intensity": 0.72,
        "Nuclide": "Ra-228 (B- 5.75 Y)"
    },
    {
        "E(keV)": 16.207,
        "Intensity": 0.159,
        "Nuclide": "Hg-195m (IT 41.6 H)"
    },
    {
        "E(keV)": 16.4,
        "Intensity": 8.29,
        "Nuclide": "Zn-72 (B- 46.5 H)"
    },
    {
        "E(keV)": 16.5,
        "Intensity": 0.306,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 17.7,
        "Intensity": 4.403e-05,
        "Nuclide": "Sn-126 (B- 1.0E5 Y)"
    },
    {
        "E(keV)": 18.07,
        "Intensity": 0.33,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 18.764,
        "Intensity": 0.04912,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 19.0,
        "Intensity": 0.374,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 19.394,
        "Intensity": 13.69,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 20.02,
        "Intensity": 0.0099,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 21.03,
        "Intensity": 0.007774,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 21.2,
        "Intensity": 0.02188,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 21.517,
        "Intensity": 2.871,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 21.543,
        "Intensity": 0.0314,
        "Nuclide": "Sm-151 (B- 90 Y)"
    },
    {
        "E(keV)": 21.646,
        "Intensity": 1.258,
        "Nuclide": "Sn-126 (B- 1.0E5 Y)"
    },
    {
        "E(keV)": 22.51,
        "Intensity": 2.308,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 22.52,
        "Intensity": 0.0496,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 22.7,
        "Intensity": 0.0999,
        "Nuclide": "Sn-126 (B- 1.0E5 Y)"
    },
    {
        "E(keV)": 23.28,
        "Intensity": 6.401,
        "Nuclide": "Sn-126 (B- 1.0E5 Y)"
    },
    {
        "E(keV)": 23.87,
        "Intensity": 16.1,
        "Nuclide": "Sb-119 (EC 38.19 H)"
    },
    {
        "E(keV)": 23.875,
        "Intensity": 16.1,
        "Nuclide": "Sn-119m (IT 293.1 D)"
    },
    {
        "E(keV)": 23.9331,
        "Intensity": 23.068,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 24.3815,
        "Intensity": 0.02688,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 24.56,
        "Intensity": 0.007675,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 25.271,
        "Intensity": 14.3,
        "Nuclide": "Sn-119m (IT 293.1 D)"
    },
    {
        "E(keV)": 25.51,
        "Intensity": 0.117,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 25.64,
        "Intensity": 14.5,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 25.64,
        "Intensity": 0.0002198,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 25.64,
        "Intensity": 12.086,
        "Nuclide": "U-231 (EC 4.2 D)"
    },
    {
        "E(keV)": 25.6515,
        "Intensity": 23.154,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 26.34,
        "Intensity": 0.008611,
        "Nuclide": "Tl-201 (EC 72.912 H)"
    },
    {
        "E(keV)": 26.3448,
        "Intensity": 2.4,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 26.3448,
        "Intensity": 0.222,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 26.348,
        "Intensity": 2.43,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 26.532,
        "Intensity": 0.316,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 26.55,
        "Intensity": 0.54,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 27.137,
        "Intensity": 0.773,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 27.36,
        "Intensity": 10.285,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 27.58,
        "Intensity": 3.525,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 27.81,
        "Intensity": 0.0279,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 28.1,
        "Intensity": 0.0013,
        "Nuclide": "Pt-195m (IT 4.02 D)"
    },
    {
        "E(keV)": 28.227,
        "Intensity": 1.132,
        "Nuclide": "Dy-166 (B- 81.6 H)"
    },
    {
        "E(keV)": 28.375,
        "Intensity": 0.11,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 28.6,
        "Intensity": 0.021,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 28.701,
        "Intensity": 0.03652,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 29.192,
        "Intensity": 0.00595,
        "Nuclide": "Pa-229 (EC 1.50 D)"
    },
    {
        "E(keV)": 29.192,
        "Intensity": 0.012,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 29.374,
        "Intensity": 15,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 29.49,
        "Intensity": 0.001584,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 29.966,
        "Intensity": 14.097,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 30.6,
        "Intensity": 0.253,
        "Nuclide": "Tl-201 (EC 72.912 H)"
    },
    {
        "E(keV)": 30.77,
        "Intensity": 0.000571,
        "Nuclide": "Nb-93m (IT 16.13 Y)"
    },
    {
        "E(keV)": 30.84,
        "Intensity": 0.007,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 30.876,
        "Intensity": 0.753,
        "Nuclide": "Au-195 (EC 186.098 D)"
    },
    {
        "E(keV)": 30.89,
        "Intensity": 2.28,
        "Nuclide": "Pt-195m (IT 4.02 D)"
    },
    {
        "E(keV)": 31.1,
        "Intensity": 0.841,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 31.14,
        "Intensity": 0.07161,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 31.444,
        "Intensity": 0.007061,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 31.5,
        "Intensity": 1.19,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 31.89,
        "Intensity": 0.0581,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 32.183,
        "Intensity": 0.0174,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 32.19,
        "Intensity": 0.258,
        "Nuclide": "Tl-201 (EC 72.912 H)"
    },
    {
        "E(keV)": 32.639,
        "Intensity": 0.211,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 32.66,
        "Intensity": 2.681,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 33.195,
        "Intensity": 0.07457,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 33.195,
        "Intensity": 0.13,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 33.196,
        "Intensity": 0.126,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 33.568,
        "Intensity": 0.2,
        "Nuclide": "Ce-144 (B- 284.9 D)"
    },
    {
        "E(keV)": 33.6,
        "Intensity": 0.101,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 34.8,
        "Intensity": 0.0024,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 34.8,
        "Intensity": 0.0024,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 35.489,
        "Intensity": 4.53,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 35.4922,
        "Intensity": 6.68,
        "Nuclide": "I-125 (EC 59.400 D)"
    },
    {
        "E(keV)": 35.504,
        "Intensity": 6.67,
        "Nuclide": "Te-125m (IT 57.40 D)"
    },
    {
        "E(keV)": 35.57,
        "Intensity": 0.421,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 36.17,
        "Intensity": 0.236,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 36.17,
        "Intensity": 0.675,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 37.09,
        "Intensity": 1.844,
        "Nuclide": "Hg-195m (IT 41.6 H)"
    },
    {
        "E(keV)": 37.138,
        "Intensity": 0.941,
        "Nuclide": "Te-121m (EC 154 D)"
    },
    {
        "E(keV)": 37.138,
        "Intensity": 0.117,
        "Nuclide": "Te-121 (EC 16.78 D)"
    },
    {
        "E(keV)": 37.15,
        "Intensity": 1.85,
        "Nuclide": "Sn-121m (B- 55 Y)"
    },
    {
        "E(keV)": 38.19,
        "Intensity": 0.16,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 38.661,
        "Intensity": 0.0105,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 38.72,
        "Intensity": 0.02483,
        "Nuclide": "Rh-105 (B- 35.36 H)"
    },
    {
        "E(keV)": 38.9,
        "Intensity": 0.11,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 39.08,
        "Intensity": 0.01402,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 39.578,
        "Intensity": 2.957,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 39.578,
        "Intensity": 7.51,
        "Nuclide": "I-129 (B- 1.57E7 Y)"
    },
    {
        "E(keV)": 39.578,
        "Intensity": 7.5,
        "Nuclide": "Xe-129m (IT 8.88 D)"
    },
    {
        "E(keV)": 39.748,
        "Intensity": 0.06832,
        "Nuclide": "Pd-103 (EC 16.991 D)"
    },
    {
        "E(keV)": 39.76,
        "Intensity": 0.06916,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 40.0,
        "Intensity": 30,
        "Nuclide": "Ra-225 (B- 14.9 D)"
    },
    {
        "E(keV)": 40.09,
        "Intensity": 0.104,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 40.35,
        "Intensity": 0.039,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 40.35,
        "Intensity": 5.038,
        "Nuclide": "Re-186m (IT 2.0E+5 Y)"
    },
    {
        "E(keV)": 40.5845,
        "Intensity": 1.053,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 40.75,
        "Intensity": 0.0264,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 40.98,
        "Intensity": 0.257,
        "Nuclide": "Ce-144 (B- 284.9 D)"
    },
    {
        "E(keV)": 41.06,
        "Intensity": 0.005893,
        "Nuclide": "Ca-47 (B- 4.536 D)"
    },
    {
        "E(keV)": 41.13,
        "Intensity": 0.304,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 41.53,
        "Intensity": 0.0108,
        "Nuclide": "Fm-252 (A 25.39 H)"
    },
    {
        "E(keV)": 41.56,
        "Intensity": 4.352,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 41.65,
        "Intensity": 0.013,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 41.79,
        "Intensity": 0.05,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 41.846,
        "Intensity": 0.005133,
        "Nuclide": "Os-191 (B- 15.4 D)"
    },
    {
        "E(keV)": 41.9,
        "Intensity": 0.829,
        "Nuclide": "Zn-72 (B- 46.5 H)"
    },
    {
        "E(keV)": 41.95,
        "Intensity": 0.35,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 41.98,
        "Intensity": 0.544,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 42.0,
        "Intensity": 0.01399,
        "Nuclide": "Cf-246 (A 35.7 H)"
    },
    {
        "E(keV)": 42.08,
        "Intensity": 7.388,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 42.33,
        "Intensity": 1.179,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 42.44,
        "Intensity": 0.04462,
        "Nuclide": "Pa-229 (EC 1.50 D)"
    },
    {
        "E(keV)": 42.44,
        "Intensity": 0.0862,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 42.641,
        "Intensity": 0.499,
        "Nuclide": "Sn-126 (B- 1.0E5 Y)"
    },
    {
        "E(keV)": 42.73,
        "Intensity": 0.0055,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 42.73,
        "Intensity": 0.002956,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 42.824,
        "Intensity": 0.02401,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 42.852,
        "Intensity": 0.01399,
        "Nuclide": "Cf-250 (A 13.08 Y)"
    },
    {
        "E(keV)": 42.88,
        "Intensity": 0.0363,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 42.9,
        "Intensity": 0.09464,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 42.98,
        "Intensity": 0.009,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 43.0,
        "Intensity": 0.0204,
        "Nuclide": "Fm-253 (A 3.00 D)"
    },
    {
        "E(keV)": 43.1,
        "Intensity": 5.4,
        "Nuclide": "Os-194 (B- 6.0 Y)"
    },
    {
        "E(keV)": 43.1,
        "Intensity": 0.06615,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 43.399,
        "Intensity": 0.01483,
        "Nuclide": "Cf-252 (A 2.645 Y)"
    },
    {
        "E(keV)": 43.423,
        "Intensity": 0.073,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 43.423,
        "Intensity": 0.003942,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 43.423,
        "Intensity": 0.024,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 43.498,
        "Intensity": 0.0395,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 43.53,
        "Intensity": 5.933,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 43.8,
        "Intensity": 0.001951,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 43.81,
        "Intensity": 25,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 43.81,
        "Intensity": 0.06018,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 43.99,
        "Intensity": 0.657,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 44.08,
        "Intensity": 0.0325,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 44.08,
        "Intensity": 0.09,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 44.17,
        "Intensity": 0.359,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 44.2,
        "Intensity": 4.165e-06,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 44.6,
        "Intensity": 0.01672,
        "Nuclide": "Np-236 (B- 154E+3 Y)"
    },
    {
        "E(keV)": 44.66,
        "Intensity": 0.13,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 44.663,
        "Intensity": 0.13,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 44.683,
        "Intensity": 12.431,
        "Nuclide": "Lu-174m (IT 142 D)"
    },
    {
        "E(keV)": 44.86,
        "Intensity": 8.33e-07,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 44.915,
        "Intensity": 0.036,
        "Nuclide": "Pu-242 (A 3.733E+5 Y)"
    },
    {
        "E(keV)": 44.988,
        "Intensity": 0.04802,
        "Nuclide": "Es-254m (B- 39.3 H)"
    },
    {
        "E(keV)": 45.23,
        "Intensity": 0.152,
        "Nuclide": "Np-236 (EC 154E+3 Y)"
    },
    {
        "E(keV)": 45.244,
        "Intensity": 0.045,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 45.2972,
        "Intensity": 1.326,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 45.299,
        "Intensity": 1.588,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 45.5,
        "Intensity": 0.32,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 46.0,
        "Intensity": 58,
        "Nuclide": "Se-72 (EC 8.40 D)"
    },
    {
        "E(keV)": 46.21,
        "Intensity": 0.000737,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 46.35,
        "Intensity": 0.223,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 46.4,
        "Intensity": 0.12,
        "Nuclide": "Cf-253 (B- 17.81 D)"
    },
    {
        "E(keV)": 46.4838,
        "Intensity": 5.762,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 46.4842,
        "Intensity": 7.98,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 46.53,
        "Intensity": 0.11,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 46.539,
        "Intensity": 4.25,
        "Nuclide": "Pb-210 (B- 22.3 Y)"
    },
    {
        "E(keV)": 46.6,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 46.8,
        "Intensity": 0.58,
        "Nuclide": "Zn-72 (B- 46.5 H)"
    },
    {
        "E(keV)": 47.05,
        "Intensity": 0.002697,
        "Nuclide": "Os-191 (B- 15.4 D)"
    },
    {
        "E(keV)": 47.155,
        "Intensity": 17.035,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 47.57,
        "Intensity": 0.066,
        "Nuclide": "Pu-236 (A 2.851 Y)"
    },
    {
        "E(keV)": 48.17,
        "Intensity": 0.103,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 48.5,
        "Intensity": 103,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 48.91562,
        "Intensity": 17.034,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 49.367,
        "Intensity": 0.188,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 49.369,
        "Intensity": 0.078,
        "Nuclide": "U-236 (A 2.3416E7 Y)"
    },
    {
        "E(keV)": 49.41,
        "Intensity": 0.13,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 49.415,
        "Intensity": 0.08081,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 49.55,
        "Intensity": 0.064,
        "Nuclide": "U-238 (A 4.468E+9 Y)"
    },
    {
        "E(keV)": 49.63,
        "Intensity": 73.7,
        "Nuclide": "Tb-156m (IT 24.4 H)"
    },
    {
        "E(keV)": 49.72,
        "Intensity": 14.96,
        "Nuclide": "Te-132 (B- 3.204 D)"
    },
    {
        "E(keV)": 49.8268,
        "Intensity": 0.36,
        "Nuclide": "Au-199 (B- 3.139 D)"
    },
    {
        "E(keV)": 49.89,
        "Intensity": 0.566,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 50.07,
        "Intensity": 0.00924,
        "Nuclide": "Es-254m (A 39.3 H)"
    },
    {
        "E(keV)": 50.13,
        "Intensity": 7.995,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 50.6,
        "Intensity": 0.003001,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 50.61,
        "Intensity": 0.535,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 50.7,
        "Intensity": 0.243,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 50.855,
        "Intensity": 0.535,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 51.01,
        "Intensity": 0.34,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 51.34,
        "Intensity": 0.0007155,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 51.624,
        "Intensity": 0.0271,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 51.72,
        "Intensity": 0.02646,
        "Nuclide": "Pa-230 (B- 17.4 D)"
    },
    {
        "E(keV)": 51.95,
        "Intensity": 0.00476,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 52.33,
        "Intensity": 0.547,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 52.5953,
        "Intensity": 5.762,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 52.5962,
        "Intensity": 2.217,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 53.1625,
        "Intensity": 2.272,
        "Nuclide": "Ba-133 (EC 10.52 Y)"
    },
    {
        "E(keV)": 53.2,
        "Intensity": 0.123,
        "Nuclide": "U-234 (A 2.457E+5 Y)"
    },
    {
        "E(keV)": 53.275,
        "Intensity": 0.443,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 53.29,
        "Intensity": 2.733e-05,
        "Nuclide": "Pd-103 (EC 16.991 D)"
    },
    {
        "E(keV)": 53.29,
        "Intensity": 0.009171,
        "Nuclide": "Hg-195m (IT 41.6 H)"
    },
    {
        "E(keV)": 53.395,
        "Intensity": 0.09981,
        "Nuclide": "Ce-144 (B- 284.9 D)"
    },
    {
        "E(keV)": 53.437,
        "Intensity": 10.34,
        "Nuclide": "As-73 (EC 80.30 D)"
    },
    {
        "E(keV)": 53.52,
        "Intensity": 0.04378,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 53.608,
        "Intensity": 0.0041,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 53.74,
        "Intensity": 0.0665,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 54.1934,
        "Intensity": 0.00846,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 54.239,
        "Intensity": 0.814,
        "Nuclide": "Dy-166 (B- 81.6 H)"
    },
    {
        "E(keV)": 54.415,
        "Intensity": 7.28,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 54.5,
        "Intensity": 0.0084,
        "Nuclide": "Tb-157 (EC 71 Y)"
    },
    {
        "E(keV)": 54.65,
        "Intensity": 0.01693,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 54.699,
        "Intensity": 0.0182,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 54.7,
        "Intensity": 183,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 54.81,
        "Intensity": 0.163,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 54.81,
        "Intensity": 0.03498,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 54.85,
        "Intensity": 0.786,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 55.03,
        "Intensity": 0.000966,
        "Nuclide": "Ac-227 (A 21.773 Y)"
    },
    {
        "E(keV)": 55.11,
        "Intensity": 0.00191,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 55.14,
        "Intensity": 0.0192,
        "Nuclide": "Fm-253 (A 3.00 D)"
    },
    {
        "E(keV)": 55.278,
        "Intensity": 2.308,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 55.4,
        "Intensity": 0.0105,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 55.56,
        "Intensity": 0.0181,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 55.56,
        "Intensity": 0.001642,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 55.698,
        "Intensity": 1.216,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 56.0,
        "Intensity": 305,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 56.32,
        "Intensity": 2.499e-06,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 56.5,
        "Intensity": 0.151,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 56.76,
        "Intensity": 9.8e-07,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 56.81,
        "Intensity": 0.0361,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 56.828,
        "Intensity": 0.00113,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 57.1,
        "Intensity": 4.64,
        "Nuclide": "Tm-167 (EC 9.25 D)"
    },
    {
        "E(keV)": 57.104,
        "Intensity": 0.39,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 57.196,
        "Intensity": 1.785,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 57.273,
        "Intensity": 0.09477,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 57.28,
        "Intensity": 0.13,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 57.3,
        "Intensity": 0.04489,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 57.356,
        "Intensity": 11.727,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 57.61,
        "Intensity": 1.223,
        "Nuclide": "Xe-127 (EC 36.4 D)"
    },
    {
        "E(keV)": 57.63,
        "Intensity": 0.502,
        "Nuclide": "Te-127m (B- 109 D)"
    },
    {
        "E(keV)": 57.75,
        "Intensity": 0.0066,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 57.78,
        "Intensity": 0.2,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 57.85,
        "Intensity": 0.0052,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 57.9805,
        "Intensity": 0.06662,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 58.0,
        "Intensity": 2.22,
        "Nuclide": "Dy-159 (EC 144.4 D)"
    },
    {
        "E(keV)": 58.0,
        "Intensity": 421,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 58.4,
        "Intensity": 0.26,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 58.5,
        "Intensity": 8.4e-06,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 58.54,
        "Intensity": 0.443,
        "Nuclide": "U-231 (EC 4.2 D)"
    },
    {
        "E(keV)": 58.57,
        "Intensity": 0.48,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 58.8,
        "Intensity": 0.27,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 59.009,
        "Intensity": 17.829,
        "Nuclide": "Re-186m (IT 2.0E+5 Y)"
    },
    {
        "E(keV)": 59.03,
        "Intensity": 0.0009759,
        "Nuclide": "Ce-144 (B- 284.9 D)"
    },
    {
        "E(keV)": 59.05,
        "Intensity": 1.205,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 59.08,
        "Intensity": 0.02876,
        "Nuclide": "Lu-174m (IT 142 D)"
    },
    {
        "E(keV)": 59.243,
        "Intensity": 0.02224,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 59.536,
        "Intensity": 34.5,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 59.5412,
        "Intensity": 35.9,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 59.5412,
        "Intensity": 3.285,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 59.692,
        "Intensity": 2.694,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 59.908,
        "Intensity": 1.225,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 59.98,
        "Intensity": 0.069,
        "Nuclide": "Er-160 (EC 28.58 H)"
    },
    {
        "E(keV)": 60.0086,
        "Intensity": 1.13,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 60.012,
        "Intensity": 1.098,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 60.3,
        "Intensity": 0.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 60.5,
        "Intensity": 23.79,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 60.65,
        "Intensity": 1.282,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 61.1,
        "Intensity": 1.435,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 61.22,
        "Intensity": 12.15,
        "Nuclide": "Sm-145 (EC 340 D)"
    },
    {
        "E(keV)": 61.46,
        "Intensity": 1.29,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 61.5,
        "Intensity": 0.56,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 61.6,
        "Intensity": 1.447,
        "Nuclide": "Fm-257 (A 100.5 D)"
    },
    {
        "E(keV)": 61.6,
        "Intensity": 0.279,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 62.09,
        "Intensity": 0.00104,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 62.17,
        "Intensity": 0.169,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 62.2,
        "Intensity": 7.95e-05,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 62.41,
        "Intensity": 0.001038,
        "Nuclide": "Pd-103 (EC 16.991 D)"
    },
    {
        "E(keV)": 62.524,
        "Intensity": 0.206,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 62.7,
        "Intensity": 0.33,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 62.86,
        "Intensity": 0.02112,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 62.95,
        "Intensity": 0.447,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 63.0,
        "Intensity": 2,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 63.0,
        "Intensity": 0.156,
        "Nuclide": "Fm-253 (A 3.00 D)"
    },
    {
        "E(keV)": 63.012,
        "Intensity": 2.139,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 63.12077,
        "Intensity": 44.02,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 63.29,
        "Intensity": 4.838,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 63.5,
        "Intensity": 0.0002027,
        "Nuclide": "Po-208 (EC 2.898 Y)"
    },
    {
        "E(keV)": 63.58,
        "Intensity": 0.109,
        "Nuclide": "W-188 (B- 69.4 D)"
    },
    {
        "E(keV)": 63.81,
        "Intensity": 0.263,
        "Nuclide": "Th-232 (A 14.05E+9 Y)"
    },
    {
        "E(keV)": 63.86,
        "Intensity": 1.036e-07,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 63.98,
        "Intensity": 10.844,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 64.281,
        "Intensity": 9.62,
        "Nuclide": "Sn-126 (B- 1.0E5 Y)"
    },
    {
        "E(keV)": 64.42,
        "Intensity": 0.274,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 64.7,
        "Intensity": 0.04512,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 64.83,
        "Intensity": 1.282,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 64.88,
        "Intensity": 1.89,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 65.36,
        "Intensity": 0.0114,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 65.4,
        "Intensity": 0.9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 65.4,
        "Intensity": 0.9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 65.548,
        "Intensity": 0.259,
        "Nuclide": "Te-121 (EC 16.78 D)"
    },
    {
        "E(keV)": 65.66,
        "Intensity": 0.0198,
        "Nuclide": "Sn-119m (IT 293.1 D)"
    },
    {
        "E(keV)": 65.72201,
        "Intensity": 2.925,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 66.0518,
        "Intensity": 1.106,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 66.3,
        "Intensity": 19,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 66.6,
        "Intensity": 0.255,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 66.72,
        "Intensity": 2.466,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 66.731,
        "Intensity": 0.14,
        "Nuclide": "Tm-171 (B- 1.92 Y)"
    },
    {
        "E(keV)": 66.84,
        "Intensity": 0.00097,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 66.881,
        "Intensity": 4.786,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 66.898,
        "Intensity": 0.02111,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 67.058,
        "Intensity": 7.249,
        "Nuclide": "Lu-174m (IT 142 D)"
    },
    {
        "E(keV)": 67.2,
        "Intensity": 0.553,
        "Nuclide": "Pm-145 (EC 17.7 Y)"
    },
    {
        "E(keV)": 67.35,
        "Intensity": 6.023,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 67.6,
        "Intensity": 0.0185,
        "Nuclide": "Ac-226 (EC 29.37 H)"
    },
    {
        "E(keV)": 67.672,
        "Intensity": 0.377,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 67.75001,
        "Intensity": 41.217,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 67.8,
        "Intensity": 0.14,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 67.8,
        "Intensity": 0.00648,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 67.85,
        "Intensity": 21.923,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 67.86,
        "Intensity": 0.092,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 67.875,
        "Intensity": 94.372,
        "Nuclide": "Ti-44 (EC 63 Y)"
    },
    {
        "E(keV)": 67.9,
        "Intensity": 0.007344,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 68.0,
        "Intensity": 0.2,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 68.0,
        "Intensity": 0.782,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 68.107,
        "Intensity": 3.292,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 68.2557,
        "Intensity": 0.01634,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 68.5,
        "Intensity": 0.00554,
        "Nuclide": "U-231 (EC 4.2 D)"
    },
    {
        "E(keV)": 68.8,
        "Intensity": 114,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 69.21,
        "Intensity": 0.006486,
        "Nuclide": "Ac-227 (A 21.773 Y)"
    },
    {
        "E(keV)": 69.528,
        "Intensity": 0.77,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 69.528,
        "Intensity": 3.554,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 69.673,
        "Intensity": 4.845,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 69.673,
        "Intensity": 2.433,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 69.76,
        "Intensity": 0.0029,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 69.76,
        "Intensity": 0.0001577,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 69.99,
        "Intensity": 0.948,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 70.65,
        "Intensity": 0.122,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 70.8814,
        "Intensity": 1.87,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 71.3,
        "Intensity": 0.0429,
        "Nuclide": "Es-254m (A 39.3 H)"
    },
    {
        "E(keV)": 71.313,
        "Intensity": 0.275,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 71.6,
        "Intensity": 2.842e-06,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 71.646,
        "Intensity": 0.154,
        "Nuclide": "Lu-177 (B- 6.73 D)"
    },
    {
        "E(keV)": 71.819,
        "Intensity": 0.0024,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 72.2,
        "Intensity": 0.6,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 72.23,
        "Intensity": 0.565,
        "Nuclide": "Ac-226 (B- 29.37 H)"
    },
    {
        "E(keV)": 72.386,
        "Intensity": 1.989,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 72.4,
        "Intensity": 1.85,
        "Nuclide": "Pm-145 (EC 17.7 Y)"
    },
    {
        "E(keV)": 72.4,
        "Intensity": 0.07,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 72.52,
        "Intensity": 0.08208,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 72.7,
        "Intensity": 0.11,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 72.751,
        "Intensity": 0.251,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 72.983,
        "Intensity": 0.01403,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 73.0,
        "Intensity": 0.3,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 73.04,
        "Intensity": 3.239,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 73.3,
        "Intensity": 0.005967,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 73.86,
        "Intensity": 0.315,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 73.92,
        "Intensity": 0.01716,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 74.4,
        "Intensity": 0.0004026,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 74.56711,
        "Intensity": 10.2,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 74.57,
        "Intensity": 0.02231,
        "Nuclide": "Pa-229 (EC 1.50 D)"
    },
    {
        "E(keV)": 74.66,
        "Intensity": 68.2,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 74.78,
        "Intensity": 50.345,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 74.94,
        "Intensity": 0.118,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 75.0,
        "Intensity": 0.2,
        "Nuclide": "Fm-257 (A 100.5 D)"
    },
    {
        "E(keV)": 75.09,
        "Intensity": 0.605,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 75.12,
        "Intensity": 0.03456,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 75.354,
        "Intensity": 1.39,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 75.42213,
        "Intensity": 0.349,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 75.42213,
        "Intensity": 0.07877,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 75.6,
        "Intensity": 0.0054,
        "Nuclide": "Cf-254 (SF 60.5 D)"
    },
    {
        "E(keV)": 75.64,
        "Intensity": 0.18,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 75.7,
        "Intensity": 2.992,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 75.7,
        "Intensity": 1.11,
        "Nuclide": "Pm-148m (IT 41.29 D)"
    },
    {
        "E(keV)": 75.8,
        "Intensity": 0.00059,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 75.8,
        "Intensity": 0.0003154,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 75.878,
        "Intensity": 6.067,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 76.073,
        "Intensity": 0.91,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 76.073,
        "Intensity": 1.169e-08,
        "Nuclide": "Pm-147 (B- 2.6234 Y)"
    },
    {
        "E(keV)": 76.39,
        "Intensity": 0.0116,
        "Nuclide": "Pa-229 (EC 1.50 D)"
    },
    {
        "E(keV)": 76.468,
        "Intensity": 5.909,
        "Nuclide": "Lu-174 (EC 3.31 Y)"
    },
    {
        "E(keV)": 76.468,
        "Intensity": 0.06384,
        "Nuclide": "Lu-174m (EC 142 D)"
    },
    {
        "E(keV)": 76.5,
        "Intensity": 496,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 76.54,
        "Intensity": 0.02332,
        "Nuclide": "Gd-146 (EC 48.27 D)"
    },
    {
        "E(keV)": 76.9,
        "Intensity": 0.0023,
        "Nuclide": "Cf-254 (SF 60.5 D)"
    },
    {
        "E(keV)": 77.1,
        "Intensity": 2.107e-05,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 77.351,
        "Intensity": 18.7,
        "Nuclide": "Hg-197 (EC 64.14 H)"
    },
    {
        "E(keV)": 77.422,
        "Intensity": 0.05967,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 77.592,
        "Intensity": 0.00041,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 78.337,
        "Intensity": 96.2,
        "Nuclide": "Ti-44 (EC 63 Y)"
    },
    {
        "E(keV)": 78.63,
        "Intensity": 12.011,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 78.7,
        "Intensity": 0.003462,
        "Nuclide": "Tm-170 (EC 128.6 D)"
    },
    {
        "E(keV)": 78.733,
        "Intensity": 0.735,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 78.7426,
        "Intensity": 10.821,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 78.75,
        "Intensity": 6.54,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 79.0,
        "Intensity": 0.001728,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 79.131,
        "Intensity": 6.629,
        "Nuclide": "Ag-108m (IT 418 Y)"
    },
    {
        "E(keV)": 79.25,
        "Intensity": 0.15,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 79.4,
        "Intensity": 0.00048,
        "Nuclide": "Dy-159 (EC 144.4 D)"
    },
    {
        "E(keV)": 79.4,
        "Intensity": 1.741,
        "Nuclide": "Zn-72 (B- 46.5 H)"
    },
    {
        "E(keV)": 79.513,
        "Intensity": 11.583,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 79.6139,
        "Intensity": 2.706,
        "Nuclide": "Ba-133 (EC 10.52 Y)"
    },
    {
        "E(keV)": 79.623,
        "Intensity": 0.27,
        "Nuclide": "Xe-133 (B- 5.243 D)"
    },
    {
        "E(keV)": 79.72,
        "Intensity": 1.894,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 79.804,
        "Intensity": 10.928,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 79.9,
        "Intensity": 0.00363,
        "Nuclide": "Es-254m (A 39.3 H)"
    },
    {
        "E(keV)": 80.12,
        "Intensity": 1.364,
        "Nuclide": "Ce-144 (B- 284.9 D)"
    },
    {
        "E(keV)": 80.185,
        "Intensity": 2.623,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 80.2,
        "Intensity": 0.08482,
        "Nuclide": "Fm-257 (A 100.5 D)"
    },
    {
        "E(keV)": 80.574,
        "Intensity": 6.71,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 80.586,
        "Intensity": 12.335,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 80.7,
        "Intensity": 0.03192,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 80.9364,
        "Intensity": 0.007613,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 80.9971,
        "Intensity": 35.184,
        "Nuclide": "Ba-133 (EC 10.52 Y)"
    },
    {
        "E(keV)": 80.997,
        "Intensity": 38,
        "Nuclide": "Xe-133 (B- 5.243 D)"
    },
    {
        "E(keV)": 81.0,
        "Intensity": 0.001775,
        "Nuclide": "Ac-226 (B- 29.37 H)"
    },
    {
        "E(keV)": 81.0,
        "Intensity": 0.00048,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 81.14,
        "Intensity": 4.144,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 81.15,
        "Intensity": 0.0003816,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 81.2,
        "Intensity": 2.1e-05,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 81.228,
        "Intensity": 0.89,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 81.3,
        "Intensity": 0.01309,
        "Nuclide": "U-231 (EC 4.2 D)"
    },
    {
        "E(keV)": 81.4,
        "Intensity": 1.567,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 81.7513,
        "Intensity": 5.126,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 81.788,
        "Intensity": 0.0478,
        "Nuclide": "Te-121m (IT 154 D)"
    },
    {
        "E(keV)": 81.8,
        "Intensity": 0.35,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 81.9,
        "Intensity": 66,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 81.99,
        "Intensity": 0.003392,
        "Nuclide": "Eu-154 (EC 8.593 Y)"
    },
    {
        "E(keV)": 82.0,
        "Intensity": 0.001242,
        "Nuclide": "Ac-227 (A 21.773 Y)"
    },
    {
        "E(keV)": 82.087,
        "Intensity": 0.4,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 82.1,
        "Intensity": 0.01813,
        "Nuclide": "U-231 (EC 4.2 D)"
    },
    {
        "E(keV)": 82.3,
        "Intensity": 0.0108,
        "Nuclide": "Os-194 (B- 6.0 Y)"
    },
    {
        "E(keV)": 82.398,
        "Intensity": 5.348,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 82.427,
        "Intensity": 0.02552,
        "Nuclide": "Os-191 (B- 15.4 D)"
    },
    {
        "E(keV)": 82.47,
        "Intensity": 13.8,
        "Nuclide": "Dy-166 (B- 81.6 H)"
    },
    {
        "E(keV)": 82.6,
        "Intensity": 0.164,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 82.86,
        "Intensity": 5.906,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 83.0,
        "Intensity": 0.1,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 83.28,
        "Intensity": 0.00539,
        "Nuclide": "Re-184m (IT 169 D)"
    },
    {
        "E(keV)": 83.3,
        "Intensity": 0.0792,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 83.36717,
        "Intensity": 0.185,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 83.36717,
        "Intensity": 0.197,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 84.0,
        "Intensity": 54.723,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 84.0,
        "Intensity": 40,
        "Nuclide": "Bk-247 (A 1380 Y)"
    },
    {
        "E(keV)": 84.18,
        "Intensity": 7.05,
        "Nuclide": "U-231 (EC 4.2 D)"
    },
    {
        "E(keV)": 84.2,
        "Intensity": 9.66e-05,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 84.214,
        "Intensity": 6.6,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 84.25474,
        "Intensity": 2.477,
        "Nuclide": "Tm-170 (B- 128.6 D)"
    },
    {
        "E(keV)": 84.262,
        "Intensity": 8.728,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 84.373,
        "Intensity": 1.22,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 84.4,
        "Intensity": 0.25,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 84.6808,
        "Intensity": 2.645,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 84.7133,
        "Intensity": 0.975,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 85.31,
        "Intensity": 0.002412,
        "Nuclide": "W-188 (B- 69.4 D)"
    },
    {
        "E(keV)": 85.59,
        "Intensity": 1.078,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 86.062,
        "Intensity": 0.15,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 86.25,
        "Intensity": 1.334,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 86.36,
        "Intensity": 5.185,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 86.37,
        "Intensity": 0.02736,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 86.4,
        "Intensity": 2.565,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 86.477,
        "Intensity": 12.4,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 86.545,
        "Intensity": 30.7,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 86.55,
        "Intensity": 31.704,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 86.68,
        "Intensity": 0.03672,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 86.71,
        "Intensity": 0.338,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 86.7882,
        "Intensity": 13.154,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 86.814,
        "Intensity": 1.97,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 86.938,
        "Intensity": 8.917,
        "Nuclide": "Sn-126 (B- 1.0E5 Y)"
    },
    {
        "E(keV)": 87.02,
        "Intensity": 0.01914,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 87.2,
        "Intensity": 0.00882,
        "Nuclide": "Ce-137m (EC 34.4 H)"
    },
    {
        "E(keV)": 87.266,
        "Intensity": 0.05322,
        "Nuclide": "Re-186m (IT 2.0E+5 Y)"
    },
    {
        "E(keV)": 87.3836,
        "Intensity": 2.701,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 87.4,
        "Intensity": 0.058,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 87.41,
        "Intensity": 0.254,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 87.567,
        "Intensity": 37,
        "Nuclide": "Sn-126 (B- 1.0E5 Y)"
    },
    {
        "E(keV)": 87.59,
        "Intensity": 1.391,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 87.63,
        "Intensity": 1.461,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 87.63,
        "Intensity": 1.461,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 87.73,
        "Intensity": 1.5e-05,
        "Nuclide": "Tm-168 (B- 93.1 D)"
    },
    {
        "E(keV)": 87.854,
        "Intensity": 0.202,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 87.941,
        "Intensity": 0.183,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 87.99,
        "Intensity": 0.14,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 88.0336,
        "Intensity": 3.7,
        "Nuclide": "Cd-109 (EC 461.4 D)"
    },
    {
        "E(keV)": 88.26,
        "Intensity": 0.08355,
        "Nuclide": "Te-127m (IT 109 D)"
    },
    {
        "E(keV)": 88.36,
        "Intensity": 14.508,
        "Nuclide": "Lu-176 (B- 4.00E10 Y)"
    },
    {
        "E(keV)": 88.5,
        "Intensity": 0.09244,
        "Nuclide": "Te-123m (IT 119.7 D)"
    },
    {
        "E(keV)": 88.7,
        "Intensity": 2.155,
        "Nuclide": "Zn-72 (B- 46.5 H)"
    },
    {
        "E(keV)": 88.862,
        "Intensity": 64.364,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 88.9656,
        "Intensity": 8.439,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 88.97,
        "Intensity": 17.67,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 89.36,
        "Intensity": 2.504,
        "Nuclide": "Hf-175 (EC 70 D)"
    },
    {
        "E(keV)": 89.48595,
        "Intensity": 0.167,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 89.48595,
        "Intensity": 0.06973,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 89.5,
        "Intensity": 0.00065,
        "Nuclide": "Tc-99 (B- 2.111E+5 Y)"
    },
    {
        "E(keV)": 89.58,
        "Intensity": 0.02185,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 89.76,
        "Intensity": 29.166,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 89.8,
        "Intensity": 79.5,
        "Nuclide": "Sb-120 (EC 5.76 D)"
    },
    {
        "E(keV)": 89.9,
        "Intensity": 184,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 89.95,
        "Intensity": 0.94,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 89.958,
        "Intensity": 9.8e-07,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 90.644,
        "Intensity": 4.649,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 90.7,
        "Intensity": 5.985,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 90.7,
        "Intensity": 0.00066,
        "Nuclide": "Es-254m (A 39.3 H)"
    },
    {
        "E(keV)": 91.105,
        "Intensity": 27.9,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 91.266,
        "Intensity": 7,
        "Nuclide": "Cu-67 (B- 61.83 H)"
    },
    {
        "E(keV)": 91.266,
        "Intensity": 3.154,
        "Nuclide": "Ga-67 (EC 3.2612 D)"
    },
    {
        "E(keV)": 91.3,
        "Intensity": 0.128,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 91.6,
        "Intensity": 3.96,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 92.19,
        "Intensity": 0.718,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 92.2,
        "Intensity": 1.4e-06,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 92.38,
        "Intensity": 2.812,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 92.5,
        "Intensity": 0.004131,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 92.51,
        "Intensity": 0.326,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 92.8,
        "Intensity": 2.772,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 93.185,
        "Intensity": 17.22,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 93.311,
        "Intensity": 16.1,
        "Nuclide": "Cu-67 (B- 61.83 H)"
    },
    {
        "E(keV)": 93.311,
        "Intensity": 39.127,
        "Nuclide": "Ga-67 (EC 3.2612 D)"
    },
    {
        "E(keV)": 93.329,
        "Intensity": 0.649,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 93.6,
        "Intensity": 0.001008,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 93.61514,
        "Intensity": 2.595,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 93.82,
        "Intensity": 0.0361,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 93.93,
        "Intensity": 1.365,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 94.64,
        "Intensity": 0.6,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 94.86,
        "Intensity": 0.00216,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 94.9,
        "Intensity": 100,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 95.24,
        "Intensity": 0.385,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 96.0,
        "Intensity": 0.012,
        "Nuclide": "Cf-246 (A 35.7 H)"
    },
    {
        "E(keV)": 96.09,
        "Intensity": 0.086,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 96.1,
        "Intensity": 426,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 96.2,
        "Intensity": 0.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 96.28,
        "Intensity": 0.03564,
        "Nuclide": "Fm-252 (A 25.39 H)"
    },
    {
        "E(keV)": 96.3,
        "Intensity": 0.00561,
        "Nuclide": "Es-254m (A 39.3 H)"
    },
    {
        "E(keV)": 96.5,
        "Intensity": 0.314,
        "Nuclide": "Tc-97m (IT 90.1 D)"
    },
    {
        "E(keV)": 96.517,
        "Intensity": 3.594,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 96.7,
        "Intensity": 0.181,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 96.734,
        "Intensity": 3.401,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 96.75,
        "Intensity": 0.116,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 96.8825,
        "Intensity": 0.002042,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 97.134,
        "Intensity": 0.0203,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 97.21,
        "Intensity": 69.3,
        "Nuclide": "Au-198m (IT 2.27 D)"
    },
    {
        "E(keV)": 97.431,
        "Intensity": 0.846,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 97.431,
        "Intensity": 29.174,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 97.89,
        "Intensity": 0.08,
        "Nuclide": "Hf-182 (B- 9E6 Y)"
    },
    {
        "E(keV)": 98.09,
        "Intensity": 0.00097,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 98.2,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 98.37,
        "Intensity": 0.353,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 98.4,
        "Intensity": 12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 98.48,
        "Intensity": 2.464,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 98.5,
        "Intensity": 0.009548,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 98.78,
        "Intensity": 0.00122,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 98.86,
        "Intensity": 0.001617,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 98.88,
        "Intensity": 10.906,
        "Nuclide": "Au-195 (EC 186.098 D)"
    },
    {
        "E(keV)": 98.9,
        "Intensity": 1.577,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 98.9,
        "Intensity": 11.4,
        "Nuclide": "Pt-195m (IT 4.02 D)"
    },
    {
        "E(keV)": 98.918,
        "Intensity": 4.295,
        "Nuclide": "Tb-158 (B- 180 Y)"
    },
    {
        "E(keV)": 98.97,
        "Intensity": 0.0203,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 98.97,
        "Intensity": 0.001971,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 99.0791,
        "Intensity": 6.673,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 99.0804,
        "Intensity": 2.695,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 99.278,
        "Intensity": 0.12,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 99.28,
        "Intensity": 2.8e-06,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 99.289,
        "Intensity": 4.224,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 99.362,
        "Intensity": 1.073,
        "Nuclide": "Re-186m (IT 2.0E+5 Y)"
    },
    {
        "E(keV)": 99.63,
        "Intensity": 0.621,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 99.853,
        "Intensity": 0.00735,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 99.91,
        "Intensity": 1.014,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 99.961,
        "Intensity": 0.03992,
        "Nuclide": "Ce-144 (B- 284.9 D)"
    },
    {
        "E(keV)": 100.0,
        "Intensity": 0.009108,
        "Nuclide": "Ac-227 (A 21.773 Y)"
    },
    {
        "E(keV)": 100.02,
        "Intensity": 2.543,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 100.1,
        "Intensity": 16.226,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 100.1065,
        "Intensity": 14.1,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 100.2,
        "Intensity": 0.0126,
        "Nuclide": "Cf-252 (A 2.645 Y)"
    },
    {
        "E(keV)": 100.724,
        "Intensity": 5.298,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 100.95,
        "Intensity": 7.105e-08,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 101.72,
        "Intensity": 0.01886,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 101.9,
        "Intensity": 0.27,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 101.93,
        "Intensity": 0.0025,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 102.06,
        "Intensity": 8.091,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 102.2,
        "Intensity": 4.2e-06,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 102.255,
        "Intensity": 6.372,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 102.27,
        "Intensity": 0.41,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 102.33,
        "Intensity": 1.869,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 102.6,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 102.8,
        "Intensity": 2.321,
        "Nuclide": "Zn-72 (B- 46.5 H)"
    },
    {
        "E(keV)": 102.8,
        "Intensity": 0.01855,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 102.82,
        "Intensity": 0.85,
        "Nuclide": "Np-236 (B- 154E+3 Y)"
    },
    {
        "E(keV)": 102.98,
        "Intensity": 0.0195,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 102.98,
        "Intensity": 0.001051,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 102.998,
        "Intensity": 0.02534,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 103.0,
        "Intensity": 0.093,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 103.065,
        "Intensity": 0.101,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 103.1,
        "Intensity": 0.39,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 103.18012,
        "Intensity": 29.8,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 103.18012,
        "Intensity": 21.239,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 103.35,
        "Intensity": 0.004158,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 103.5,
        "Intensity": 0.007812,
        "Nuclide": "Pu-242 (A 3.733E+5 Y)"
    },
    {
        "E(keV)": 103.68,
        "Intensity": 0.0001017,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 103.85,
        "Intensity": 0.0008775,
        "Nuclide": "Te-121m (EC 154 D)"
    },
    {
        "E(keV)": 103.9,
        "Intensity": 0.37,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 103.9,
        "Intensity": 0.9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 103.971,
        "Intensity": 0.87,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 104.0,
        "Intensity": 0.01023,
        "Nuclide": "Es-254m (A 39.3 H)"
    },
    {
        "E(keV)": 104.1,
        "Intensity": 61,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 104.23,
        "Intensity": 8.715,
        "Nuclide": "Np-236 (EC 154E+3 Y)"
    },
    {
        "E(keV)": 104.234,
        "Intensity": 0.00708,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 104.3,
        "Intensity": 4.68,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 104.36,
        "Intensity": 0.176,
        "Nuclide": "Es-254m (B- 39.3 H)"
    },
    {
        "E(keV)": 104.4,
        "Intensity": 0.619,
        "Nuclide": "Fm-257 (A 100.5 D)"
    },
    {
        "E(keV)": 104.62,
        "Intensity": 0.579,
        "Nuclide": "Nb-91m (IT 60.86 D)"
    },
    {
        "E(keV)": 104.729,
        "Intensity": 13.436,
        "Nuclide": "Re-184m (IT 169 D)"
    },
    {
        "E(keV)": 104.84,
        "Intensity": 3.51,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 105.2,
        "Intensity": 0.00442,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 105.305,
        "Intensity": 21.152,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 105.318,
        "Intensity": 24.846,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 105.3595,
        "Intensity": 12.344,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 105.47,
        "Intensity": 1.646,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 105.5,
        "Intensity": 0.145,
        "Nuclide": "Te-129m (IT 33.6 D)"
    },
    {
        "E(keV)": 105.8,
        "Intensity": 127,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 105.85,
        "Intensity": 0.001206,
        "Nuclide": "W-188 (B- 69.4 D)"
    },
    {
        "E(keV)": 106.02,
        "Intensity": 0.138,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 106.113,
        "Intensity": 0.07783,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 106.123,
        "Intensity": 27.2,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 106.125,
        "Intensity": 0.309,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 106.57,
        "Intensity": 0.08739,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 106.79,
        "Intensity": 0.001325,
        "Nuclide": "Ac-227 (A 21.773 Y)"
    },
    {
        "E(keV)": 107.008,
        "Intensity": 0.636,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 107.108,
        "Intensity": 0.811,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 107.9318,
        "Intensity": 10.961,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 107.9347,
        "Intensity": 2.172,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 108.0,
        "Intensity": 0.01056,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 108.41,
        "Intensity": 0.251,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 108.7,
        "Intensity": 0.068,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 108.79,
        "Intensity": 0.12,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 108.96,
        "Intensity": 2.807,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 109.0,
        "Intensity": 0.012,
        "Nuclide": "Pu-236 (A 2.851 Y)"
    },
    {
        "E(keV)": 109.16,
        "Intensity": 1.54,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 109.276,
        "Intensity": 0.274,
        "Nuclide": "Te-125m (IT 57.40 D)"
    },
    {
        "E(keV)": 109.4,
        "Intensity": 800,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 109.5,
        "Intensity": 3.762,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 109.6,
        "Intensity": 0.02433,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 109.6,
        "Intensity": 1.861,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 109.681,
        "Intensity": 0.209,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 109.7304,
        "Intensity": 2.877,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 109.758,
        "Intensity": 6.776,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 109.77987,
        "Intensity": 17.394,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 109.77987,
        "Intensity": 0.0013,
        "Nuclide": "Er-169 (B- 9.40 D)"
    },
    {
        "E(keV)": 109.9,
        "Intensity": 50,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 110.0,
        "Intensity": 5.959e-05,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 110.3,
        "Intensity": 34,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 110.4,
        "Intensity": 0.01194,
        "Nuclide": "Ir-192 (EC 73.827 D)"
    },
    {
        "E(keV)": 110.76,
        "Intensity": 0.006866,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 110.8,
        "Intensity": 1.26e-06,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 110.9291,
        "Intensity": 1.924,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 110.94,
        "Intensity": 0.04391,
        "Nuclide": "Rh-101 (EC 3.3 Y)"
    },
    {
        "E(keV)": 110.943,
        "Intensity": 1.897,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 111.1,
        "Intensity": 0.002754,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 111.109,
        "Intensity": 0.05405,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 111.207,
        "Intensity": 5.789,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 111.207,
        "Intensity": 17.104,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 111.54,
        "Intensity": 0.317,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 111.7,
        "Intensity": 8.9,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 111.76,
        "Intensity": 1.742,
        "Nuclide": "Te-132 (B- 3.204 D)"
    },
    {
        "E(keV)": 111.762,
        "Intensity": 0.298,
        "Nuclide": "Lu-174m (IT 142 D)"
    },
    {
        "E(keV)": 111.8,
        "Intensity": 1.9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 112.1,
        "Intensity": 2.072,
        "Nuclide": "Zn-72 (B- 46.5 H)"
    },
    {
        "E(keV)": 112.4,
        "Intensity": 19.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 112.7,
        "Intensity": 14,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 112.75,
        "Intensity": 0.019,
        "Nuclide": "U-236 (A 2.3416E7 Y)"
    },
    {
        "E(keV)": 112.81,
        "Intensity": 0.277,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 112.9,
        "Intensity": 7.228,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 112.9498,
        "Intensity": 20.412,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 112.9498,
        "Intensity": 6.4,
        "Nuclide": "Lu-177 (B- 6.73 D)"
    },
    {
        "E(keV)": 113.159,
        "Intensity": 0.517,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 113.5,
        "Intensity": 0.0102,
        "Nuclide": "U-238 (A 4.468E+9 Y)"
    },
    {
        "E(keV)": 113.51,
        "Intensity": 0.0161,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 113.805,
        "Intensity": 1.882,
        "Nuclide": "Yb-175 (B- 4.185 D)"
    },
    {
        "E(keV)": 113.81,
        "Intensity": 0.306,
        "Nuclide": "Hf-175 (EC 70 D)"
    },
    {
        "E(keV)": 114.0,
        "Intensity": 6.125e-06,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 114.061,
        "Intensity": 2.896,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 114.33,
        "Intensity": 2.6,
        "Nuclide": "Hf-182 (B- 9E6 Y)"
    },
    {
        "E(keV)": 114.71,
        "Intensity": 44.068,
        "Nuclide": "Gd-146 (EC 48.27 D)"
    },
    {
        "E(keV)": 114.97,
        "Intensity": 0.007371,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 115.2,
        "Intensity": 0.0385,
        "Nuclide": "Au-198m (IT 2.27 D)"
    },
    {
        "E(keV)": 115.38,
        "Intensity": 0.000462,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 115.51,
        "Intensity": 44.068,
        "Nuclide": "Gd-146 (EC 48.27 D)"
    },
    {
        "E(keV)": 115.55,
        "Intensity": 0.01824,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 115.6,
        "Intensity": 2.3,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 115.8682,
        "Intensity": 0.649,
        "Nuclide": "Lu-177m (IT 160.4 D)"
    },
    {
        "E(keV)": 116.26,
        "Intensity": 0.000597,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 116.3,
        "Intensity": 1.962,
        "Nuclide": "Te-132 (B- 3.204 D)"
    },
    {
        "E(keV)": 116.48,
        "Intensity": 0.008023,
        "Nuclide": "Ag-110m (IT 249.79 D)"
    },
    {
        "E(keV)": 116.7,
        "Intensity": 1.1,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 116.955,
        "Intensity": 0.264,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 117.1,
        "Intensity": 12.6,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 117.2,
        "Intensity": 0.0476,
        "Nuclide": "Pa-229 (EC 1.50 D)"
    },
    {
        "E(keV)": 117.6,
        "Intensity": 0.573,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 117.7,
        "Intensity": 167,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 117.702,
        "Intensity": 0.16,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 117.8,
        "Intensity": 0.00194,
        "Nuclide": "Pa-230 (B- 17.4 D)"
    },
    {
        "E(keV)": 117.9,
        "Intensity": 0.0021,
        "Nuclide": "Cf-254 (SF 60.5 D)"
    },
    {
        "E(keV)": 118.1117,
        "Intensity": 0.0001167,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 118.19018,
        "Intensity": 1.861,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 118.19018,
        "Intensity": 0.00014,
        "Nuclide": "Er-169 (B- 9.40 D)"
    },
    {
        "E(keV)": 118.837,
        "Intensity": 0.06098,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 118.968,
        "Intensity": 0.00406,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 119.0,
        "Intensity": 0.131,
        "Nuclide": "Pa-229 (EC 1.50 D)"
    },
    {
        "E(keV)": 119.18,
        "Intensity": 0.07114,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 119.32,
        "Intensity": 0.0148,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 119.4,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 119.9,
        "Intensity": 0.108,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 120.48,
        "Intensity": 0.396,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 120.8,
        "Intensity": 0.01152,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 120.816,
        "Intensity": 0.00332,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 120.9,
        "Intensity": 0.0342,
        "Nuclide": "U-234 (A 2.457E+5 Y)"
    },
    {
        "E(keV)": 121.1155,
        "Intensity": 17.1,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 121.2,
        "Intensity": 6.86e-07,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 121.2,
        "Intensity": 0.02425,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 121.22,
        "Intensity": 22.88,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 121.22,
        "Intensity": 0.00285,
        "Nuclide": "Pm-147 (B- 2.6234 Y)"
    },
    {
        "E(keV)": 121.53,
        "Intensity": 0.002125,
        "Nuclide": "Ac-227 (A 21.773 Y)"
    },
    {
        "E(keV)": 121.6,
        "Intensity": 0.0363,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 121.621,
        "Intensity": 5.915,
        "Nuclide": "Lu-177m (IT 160.4 D)"
    },
    {
        "E(keV)": 121.7817,
        "Intensity": 28.634,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 121.8,
        "Intensity": 0.005967,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 122.06065,
        "Intensity": 85.578,
        "Nuclide": "Co-57 (EC 271.74 D)"
    },
    {
        "E(keV)": 122.319,
        "Intensity": 1.192,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 122.64,
        "Intensity": 0.603,
        "Nuclide": "Re-186 (EC 3.7183 D)"
    },
    {
        "E(keV)": 122.7,
        "Intensity": 27.581,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 122.78,
        "Intensity": 0.02829,
        "Nuclide": "Hg-195m (IT 41.6 H)"
    },
    {
        "E(keV)": 122.916,
        "Intensity": 1.294,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 123.01,
        "Intensity": 0.001,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 123.071,
        "Intensity": 40.557,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 123.4,
        "Intensity": 45,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 123.8,
        "Intensity": 32,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 123.805,
        "Intensity": 28.983,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 124.55,
        "Intensity": 0.687,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 124.65,
        "Intensity": 0.739,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 124.8,
        "Intensity": 2.828e-07,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 125.0,
        "Intensity": 9.8e-07,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 125.3,
        "Intensity": 0.00408,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 125.3,
        "Intensity": 0.0003285,
        "Nuclide": "Pu-237 (EC 45.2 D)"
    },
    {
        "E(keV)": 125.358,
        "Intensity": 0.0192,
        "Nuclide": "W-185 (B- 75.1 D)"
    },
    {
        "E(keV)": 125.3581,
        "Intensity": 0.354,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 125.71,
        "Intensity": 0.003552,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 125.812,
        "Intensity": 12.815,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 125.84,
        "Intensity": 0.001192,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 126.0,
        "Intensity": 0.000495,
        "Nuclide": "Es-254m (A 39.3 H)"
    },
    {
        "E(keV)": 126.0,
        "Intensity": 1.28e-07,
        "Nuclide": "Fe-55 (EC 2.73 Y)"
    },
    {
        "E(keV)": 126.15,
        "Intensity": 8.208,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 126.2,
        "Intensity": 0.01519,
        "Nuclide": "Lu-174m (IT 142 D)"
    },
    {
        "E(keV)": 127.164,
        "Intensity": 9.398,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 127.226,
        "Intensity": 68.209,
        "Nuclide": "Rh-101 (EC 3.3 Y)"
    },
    {
        "E(keV)": 127.226,
        "Intensity": 0.599,
        "Nuclide": "Rh-101m (EC 4.34 D)"
    },
    {
        "E(keV)": 127.805,
        "Intensity": 2.126,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 127.91,
        "Intensity": 1.653,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 128.2,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 128.503,
        "Intensity": 15.535,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 128.55,
        "Intensity": 0.001387,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 129.08,
        "Intensity": 0.06819,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 129.2,
        "Intensity": 0.03,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 129.24,
        "Intensity": 0.01596,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 129.296,
        "Intensity": 0.00631,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 129.4,
        "Intensity": 3.507,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 129.431,
        "Intensity": 29,
        "Nuclide": "Os-191 (B- 15.4 D)"
    },
    {
        "E(keV)": 129.5,
        "Intensity": 0.08436,
        "Nuclide": "Pt-195m (IT 4.02 D)"
    },
    {
        "E(keV)": 129.757,
        "Intensity": 0.818,
        "Nuclide": "Au-195 (EC 186.098 D)"
    },
    {
        "E(keV)": 129.79,
        "Intensity": 2.827,
        "Nuclide": "Pt-195m (IT 4.02 D)"
    },
    {
        "E(keV)": 129.8,
        "Intensity": 0.0004993,
        "Nuclide": "Sr-85 (EC 64.84 D)"
    },
    {
        "E(keV)": 129.81,
        "Intensity": 4.34e-07,
        "Nuclide": "Kr-85 (B- 10.756 Y)"
    },
    {
        "E(keV)": 129.942,
        "Intensity": 0.535,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 130.4,
        "Intensity": 1.3,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 130.414,
        "Intensity": 0.209,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 130.5,
        "Intensity": 9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 130.52368,
        "Intensity": 11.263,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 131.101,
        "Intensity": 0.085,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 131.117,
        "Intensity": 0.467,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 131.613,
        "Intensity": 0.131,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 131.8,
        "Intensity": 0.17,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 131.93,
        "Intensity": 0.01713,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 132.2,
        "Intensity": 18.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 132.413,
        "Intensity": 3.92,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 132.687,
        "Intensity": 0.202,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 132.86,
        "Intensity": 0.262,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 132.99,
        "Intensity": 2.774,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 133.021,
        "Intensity": 43.309,
        "Nuclide": "Hf-181 (B- 42.39 D)"
    },
    {
        "E(keV)": 133.515,
        "Intensity": 11.09,
        "Nuclide": "Ce-144 (B- 284.9 D)"
    },
    {
        "E(keV)": 133.609,
        "Intensity": 2.126,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 133.7,
        "Intensity": 6.36,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 135.17,
        "Intensity": 0.01056,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 135.2,
        "Intensity": 0.003456,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 135.34,
        "Intensity": 2.568,
        "Nuclide": "Tl-201 (EC 72.912 H)"
    },
    {
        "E(keV)": 135.6,
        "Intensity": 7.882,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 135.66,
        "Intensity": 3.5e-07,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 135.664,
        "Intensity": 0.078,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 136.0001,
        "Intensity": 57.918,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 136.0,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 136.06,
        "Intensity": 0.112,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 136.09,
        "Intensity": 0.794,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 136.1,
        "Intensity": 0.009639,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 136.26,
        "Intensity": 5.852,
        "Nuclide": "Hf-181 (B- 42.39 D)"
    },
    {
        "E(keV)": 136.28,
        "Intensity": 0.03113,
        "Nuclide": "W-181 (EC 121.2 D)"
    },
    {
        "E(keV)": 136.3426,
        "Intensity": 0.199,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 136.47356,
        "Intensity": 10.677,
        "Nuclide": "Co-57 (EC 271.74 D)"
    },
    {
        "E(keV)": 136.7,
        "Intensity": 0.05987,
        "Nuclide": "Fm-257 (A 100.5 D)"
    },
    {
        "E(keV)": 136.7248,
        "Intensity": 0.048,
        "Nuclide": "Lu-177 (B- 6.73 D)"
    },
    {
        "E(keV)": 136.86,
        "Intensity": 0.861,
        "Nuclide": "Hf-181 (B- 42.39 D)"
    },
    {
        "E(keV)": 136.99,
        "Intensity": 1.18,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 137.157,
        "Intensity": 9.42,
        "Nuclide": "Re-186 (B- 3.7183 D)"
    },
    {
        "E(keV)": 137.5,
        "Intensity": 0.00011,
        "Nuclide": "Dy-159 (EC 144.4 D)"
    },
    {
        "E(keV)": 137.658,
        "Intensity": 0.103,
        "Nuclide": "Yb-175 (B- 4.185 D)"
    },
    {
        "E(keV)": 138.2,
        "Intensity": 73,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 138.5,
        "Intensity": 61,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 138.92,
        "Intensity": 4.266,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 139.03,
        "Intensity": 13.76,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 139.243,
        "Intensity": 0.009858,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 139.742,
        "Intensity": 0.07704,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 139.92,
        "Intensity": 0.192,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 140.3,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 140.35,
        "Intensity": 2.419,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 140.511,
        "Intensity": 4.524,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 140.6,
        "Intensity": 0.02998,
        "Nuclide": "Pt-195m (IT 4.02 D)"
    },
    {
        "E(keV)": 140.7,
        "Intensity": 1.165e-06,
        "Nuclide": "Rh-102m (IT 2.9 Y)"
    },
    {
        "E(keV)": 140.76,
        "Intensity": 0.22,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 140.85,
        "Intensity": 0.00216,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 140.88,
        "Intensity": 0.021,
        "Nuclide": "Th-232 (A 14.05E+9 Y)"
    },
    {
        "E(keV)": 141.0,
        "Intensity": 3.108e-06,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 141.1,
        "Intensity": 0.006308,
        "Nuclide": "Tl-201 (EC 72.912 H)"
    },
    {
        "E(keV)": 141.1,
        "Intensity": 78,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 141.78,
        "Intensity": 0.006432,
        "Nuclide": "W-188 (B- 69.4 D)"
    },
    {
        "E(keV)": 141.8,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 141.89,
        "Intensity": 0.12,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 141.91,
        "Intensity": 1.076,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 142.0,
        "Intensity": 1.342e-06,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 142.2,
        "Intensity": 8.151,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 142.5,
        "Intensity": 0.64,
        "Nuclide": "Cf-254 (SF 60.5 D)"
    },
    {
        "E(keV)": 142.652,
        "Intensity": 1.02,
        "Nuclide": "Fe-59 (B- 44.503 D)"
    },
    {
        "E(keV)": 143.17,
        "Intensity": 7.4e-07,
        "Nuclide": "Re-186 (B- 3.7183 D)"
    },
    {
        "E(keV)": 143.249,
        "Intensity": 0.43,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 143.76,
        "Intensity": 10.96,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 143.8,
        "Intensity": 0.01015,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 143.872,
        "Intensity": 0.04878,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 144.0,
        "Intensity": 0.1,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 144.0,
        "Intensity": 0.01113,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 144.1247,
        "Intensity": 2.492,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 144.232,
        "Intensity": 3.22,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 144.3,
        "Intensity": 36,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 144.6,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 144.7,
        "Intensity": 51,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 144.7,
        "Intensity": 82.9,
        "Nuclide": "Zn-72 (B- 46.5 H)"
    },
    {
        "E(keV)": 144.78,
        "Intensity": 3.9e-07,
        "Nuclide": "Te-125m (IT 57.40 D)"
    },
    {
        "E(keV)": 144.8,
        "Intensity": 0.192,
        "Nuclide": "Fm-253 (A 3.00 D)"
    },
    {
        "E(keV)": 144.863,
        "Intensity": 0.328,
        "Nuclide": "Yb-175 (B- 4.185 D)"
    },
    {
        "E(keV)": 144.9,
        "Intensity": 68,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 145.17,
        "Intensity": 0.146,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 145.252,
        "Intensity": 4.29,
        "Nuclide": "Xe-127 (EC 36.4 D)"
    },
    {
        "E(keV)": 145.4405,
        "Intensity": 48.2,
        "Nuclide": "Ce-141 (B- 32.50 D)"
    },
    {
        "E(keV)": 146.0,
        "Intensity": 0.003499,
        "Nuclide": "Cf-246 (A 35.7 H)"
    },
    {
        "E(keV)": 146.061,
        "Intensity": 0.05188,
        "Nuclide": "Eu-155 (B- 4.7611 Y)"
    },
    {
        "E(keV)": 146.15,
        "Intensity": 26.972,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 146.2,
        "Intensity": 0.218,
        "Nuclide": "Pm-146 (EC 5.53 Y)"
    },
    {
        "E(keV)": 146.212,
        "Intensity": 0.08947,
        "Nuclide": "Ti-44 (EC 63 Y)"
    },
    {
        "E(keV)": 146.273,
        "Intensity": 0.004435,
        "Nuclide": "Re-186m (IT 2.0E+5 Y)"
    },
    {
        "E(keV)": 146.345,
        "Intensity": 0.00657,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 146.4,
        "Intensity": 0.09817,
        "Nuclide": "Pa-229 (EC 1.50 D)"
    },
    {
        "E(keV)": 146.6,
        "Intensity": 480,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 146.7,
        "Intensity": 5.52,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 147.09,
        "Intensity": 1.243,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 147.09,
        "Intensity": 0.108,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 147.164,
        "Intensity": 3.51,
        "Nuclide": "Lu-177m (IT 160.4 D)"
    },
    {
        "E(keV)": 147.48,
        "Intensity": 0.003091,
        "Nuclide": "Ac-227 (A 21.773 Y)"
    },
    {
        "E(keV)": 147.8,
        "Intensity": 35.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 148.15,
        "Intensity": 0.882,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 148.2,
        "Intensity": 0.01844,
        "Nuclide": "Pa-229 (EC 1.50 D)"
    },
    {
        "E(keV)": 148.567,
        "Intensity": 0.0001855,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 148.64,
        "Intensity": 2.621,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 149.4,
        "Intensity": 9.3,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 149.42,
        "Intensity": 0.0575,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 149.71,
        "Intensity": 5.17,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 149.735,
        "Intensity": 51.132,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 149.84,
        "Intensity": 0.787,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 149.84,
        "Intensity": 0.08493,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 150.0,
        "Intensity": 0.02,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 150.04,
        "Intensity": 0.796,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 150.059,
        "Intensity": 10.842,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 150.3,
        "Intensity": 0.9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 150.6,
        "Intensity": 32,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 150.81,
        "Intensity": 0.00282,
        "Nuclide": "In-111 (EC 2.8047 D)"
    },
    {
        "E(keV)": 150.93,
        "Intensity": 0.076,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 151.18,
        "Intensity": 2.17e-06,
        "Nuclide": "Kr-85 (B- 10.756 Y)"
    },
    {
        "E(keV)": 151.18,
        "Intensity": 0.001198,
        "Nuclide": "Sr-85 (EC 64.84 D)"
    },
    {
        "E(keV)": 151.3,
        "Intensity": 0.07296,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 151.414,
        "Intensity": 0.232,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 151.6245,
        "Intensity": 0.01132,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 151.8,
        "Intensity": 100,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 151.88,
        "Intensity": 0.334,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 152.1,
        "Intensity": 3.12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 152.2,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 152.32,
        "Intensity": 0.008309,
        "Nuclide": "W-181 (EC 121.2 D)"
    },
    {
        "E(keV)": 152.43,
        "Intensity": 8.393,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 152.4308,
        "Intensity": 6.928,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 152.63,
        "Intensity": 0.00098,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 152.7,
        "Intensity": 0.912,
        "Nuclide": "Es-251 (EC 33 H)"
    },
    {
        "E(keV)": 152.72,
        "Intensity": 0.000937,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 152.75,
        "Intensity": 0.001377,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 153.246,
        "Intensity": 5.753,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 153.2843,
        "Intensity": 16.92,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 153.59,
        "Intensity": 65.338,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 153.6,
        "Intensity": 6.242,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 153.84,
        "Intensity": 0.00459,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 153.92,
        "Intensity": 0.187,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 154.0,
        "Intensity": 0.0558,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 154.0,
        "Intensity": 0.2,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 154.0,
        "Intensity": 0.03338,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 154.21,
        "Intensity": 5.617,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 154.23,
        "Intensity": 0.000753,
        "Nuclide": "Ac-226 (B- 29.37 H)"
    },
    {
        "E(keV)": 154.23,
        "Intensity": 0.125,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 154.336,
        "Intensity": 0.77,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 154.4,
        "Intensity": 5.742,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 154.57,
        "Intensity": 46.633,
        "Nuclide": "Gd-146 (EC 48.27 D)"
    },
    {
        "E(keV)": 154.6,
        "Intensity": 17.226,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 154.6,
        "Intensity": 0.06,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 154.7,
        "Intensity": 280,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 154.72,
        "Intensity": 0.167,
        "Nuclide": "Hf-172 (EC 1.87 Y)"
    },
    {
        "E(keV)": 155.0,
        "Intensity": 19.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 155.05,
        "Intensity": 31.255,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 155.239,
        "Intensity": 0.092,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 156.02,
        "Intensity": 2.113,
        "Nuclide": "Sn-117m (IT 13.60 D)"
    },
    {
        "E(keV)": 156.09,
        "Intensity": 7,
        "Nuclide": "Hf-182 (B- 9E6 Y)"
    },
    {
        "E(keV)": 156.3876,
        "Intensity": 2.642,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 156.409,
        "Intensity": 1.19,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 157.26,
        "Intensity": 0.36,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 157.41,
        "Intensity": 0.241,
        "Nuclide": "Rh-101m (IT 4.34 D)"
    },
    {
        "E(keV)": 157.42,
        "Intensity": 0.0014,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 158.027,
        "Intensity": 0.01702,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 158.05,
        "Intensity": 17.48,
        "Nuclide": "Ac-226 (B- 29.37 H)"
    },
    {
        "E(keV)": 158.18,
        "Intensity": 0.07,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 158.35,
        "Intensity": 3.959,
        "Nuclide": "Np-236 (B- 154E+3 Y)"
    },
    {
        "E(keV)": 158.37947,
        "Intensity": 40,
        "Nuclide": "Au-199 (B- 3.139 D)"
    },
    {
        "E(keV)": 158.38,
        "Intensity": 100.055,
        "Nuclide": "Ni-56 (EC 6.075 D)"
    },
    {
        "E(keV)": 158.42,
        "Intensity": 0.035,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 158.56,
        "Intensity": 86.4,
        "Nuclide": "Sn-117m (IT 13.60 D)"
    },
    {
        "E(keV)": 158.633,
        "Intensity": 0.685,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 158.7,
        "Intensity": 0.78,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 158.7,
        "Intensity": 10,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 158.782,
        "Intensity": 0.01892,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 158.785,
        "Intensity": 0.03917,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 158.8,
        "Intensity": 0.0004536,
        "Nuclide": "Pu-242 (A 3.733E+5 Y)"
    },
    {
        "E(keV)": 158.87,
        "Intensity": 1.751,
        "Nuclide": "Pd-100 (EC 3.63 D)"
    },
    {
        "E(keV)": 158.9,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 159.0,
        "Intensity": 84.04,
        "Nuclide": "Te-123m (IT 119.7 D)"
    },
    {
        "E(keV)": 159.381,
        "Intensity": 68.3,
        "Nuclide": "Sc-47 (B- 3.3492 D)"
    },
    {
        "E(keV)": 159.5,
        "Intensity": 7.7,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 159.71,
        "Intensity": 0.01306,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 159.955,
        "Intensity": 6.541e-06,
        "Nuclide": "Pu-241 (A 14.35 Y)"
    },
    {
        "E(keV)": 160.0,
        "Intensity": 0.001938,
        "Nuclide": "Cf-252 (A 2.645 Y)"
    },
    {
        "E(keV)": 160.26,
        "Intensity": 0.005796,
        "Nuclide": "Ac-227 (A 21.773 Y)"
    },
    {
        "E(keV)": 160.308,
        "Intensity": 0.000402,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 160.33,
        "Intensity": 0.001932,
        "Nuclide": "Sn-123 (B- 129.2 D)"
    },
    {
        "E(keV)": 160.33,
        "Intensity": 37.889,
        "Nuclide": "Np-236 (EC 154E+3 Y)"
    },
    {
        "E(keV)": 160.51,
        "Intensity": 0.773,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 160.5271,
        "Intensity": 2.921,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 160.5309,
        "Intensity": 0.595,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 160.6109,
        "Intensity": 0.666,
        "Nuclide": "Ba-133 (EC 10.52 Y)"
    },
    {
        "E(keV)": 160.613,
        "Intensity": 0.066,
        "Nuclide": "Xe-133 (B- 5.243 D)"
    },
    {
        "E(keV)": 161.269,
        "Intensity": 6.493,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 161.29,
        "Intensity": 2.728,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 161.3,
        "Intensity": 0.02364,
        "Nuclide": "Hf-175 (EC 70 D)"
    },
    {
        "E(keV)": 161.3465,
        "Intensity": 8.924,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 161.3487,
        "Intensity": 0.607,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 161.6,
        "Intensity": 0.00855,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 161.83,
        "Intensity": 1.095,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 161.86,
        "Intensity": 0.01281,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 161.932,
        "Intensity": 0.146,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 162.0,
        "Intensity": 99,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 162.3,
        "Intensity": 100,
        "Nuclide": "Cf,248CM-252 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 162.306,
        "Intensity": 0.23,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 162.321,
        "Intensity": 4.878,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 162.3266,
        "Intensity": 23.333,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 162.37,
        "Intensity": 0.01189,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 162.4,
        "Intensity": 100,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 162.66,
        "Intensity": 6.219,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 162.852,
        "Intensity": 0.587,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 163.101,
        "Intensity": 0.155,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 163.24,
        "Intensity": 0.02387,
        "Nuclide": "Am-242m (A 141 Y)"
    },
    {
        "E(keV)": 163.28,
        "Intensity": 4.395,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 163.3,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 163.33,
        "Intensity": 5.08,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 163.5,
        "Intensity": 0.096,
        "Nuclide": "Es-251 (EC 33 H)"
    },
    {
        "E(keV)": 163.58,
        "Intensity": 1.553,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 163.92,
        "Intensity": 3.39,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 163.93,
        "Intensity": 1.95,
        "Nuclide": "Xe-131m (IT 11.84 D)"
    },
    {
        "E(keV)": 164.0,
        "Intensity": 32,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 164.0,
        "Intensity": 0.37,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 164.013,
        "Intensity": 0.674,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 164.05,
        "Intensity": 0.008658,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 164.3,
        "Intensity": 5.623,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 164.34,
        "Intensity": 1.281,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 164.5,
        "Intensity": 17.82,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 164.522,
        "Intensity": 0.00623,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 164.61,
        "Intensity": 1.86,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 164.8,
        "Intensity": 0.442,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 165.0,
        "Intensity": 0.00066,
        "Nuclide": "Pu-236 (A 2.851 Y)"
    },
    {
        "E(keV)": 165.0,
        "Intensity": 7e-07,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 165.0,
        "Intensity": 0.143,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 165.0134,
        "Intensity": 2.163,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 165.049,
        "Intensity": 3.015,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 165.3,
        "Intensity": 0.00855,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 165.5,
        "Intensity": 0.0084,
        "Nuclide": "Bk-245 (A 4.94 D)"
    },
    {
        "E(keV)": 165.853,
        "Intensity": 79.887,
        "Nuclide": "Ce-139 (EC 137.640 D)"
    },
    {
        "E(keV)": 165.88,
        "Intensity": 0.155,
        "Nuclide": "Tl-201 (EC 72.912 H)"
    },
    {
        "E(keV)": 166.369,
        "Intensity": 0.01696,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 166.41,
        "Intensity": 0.104,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 166.5548,
        "Intensity": 0.0002917,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 166.576,
        "Intensity": 0.369,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 166.7,
        "Intensity": 0.28,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 167.1,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 167.43,
        "Intensity": 10.013,
        "Nuclide": "Tl-201 (EC 72.912 H)"
    },
    {
        "E(keV)": 167.5,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 167.75,
        "Intensity": 8.325,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 169.0,
        "Intensity": 0.001364,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 169.0,
        "Intensity": 0.227,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 169.15,
        "Intensity": 11.19,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 169.156,
        "Intensity": 0.073,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 169.26,
        "Intensity": 0.439,
        "Nuclide": "Ce-137m (EC 34.4 H)"
    },
    {
        "E(keV)": 169.3,
        "Intensity": 4.56,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 169.78,
        "Intensity": 19.334,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 169.9,
        "Intensity": 0.00192,
        "Nuclide": "Pa-229 (A 1.50 D)"
    },
    {
        "E(keV)": 170.42,
        "Intensity": 6.341,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 171.28,
        "Intensity": 90.249,
        "Nuclide": "In-111 (EC 2.8047 D)"
    },
    {
        "E(keV)": 171.393,
        "Intensity": 2.938,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 171.56,
        "Intensity": 100,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 171.8576,
        "Intensity": 4.809,
        "Nuclide": "Lu-177m (IT 160.4 D)"
    },
    {
        "E(keV)": 171.9,
        "Intensity": 0.00127,
        "Nuclide": "Ac-227 (A 21.773 Y)"
    },
    {
        "E(keV)": 172.0,
        "Intensity": 192,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 172.132,
        "Intensity": 25.548,
        "Nuclide": "Xe-127 (EC 36.4 D)"
    },
    {
        "E(keV)": 172.19,
        "Intensity": 3.857,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 172.2,
        "Intensity": 18.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 172.3035,
        "Intensity": 0.0002042,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 172.5,
        "Intensity": 10,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 172.54,
        "Intensity": 0.2,
        "Nuclide": "Hf-182 (B- 9E6 Y)"
    },
    {
        "E(keV)": 172.719,
        "Intensity": 0.193,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 172.85307,
        "Intensity": 0.08046,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 172.85307,
        "Intensity": 0.03618,
        "Nuclide": "Gd-153 (EC 240.4 D)"
    },
    {
        "E(keV)": 174.166,
        "Intensity": 9.8e-08,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 174.3991,
        "Intensity": 12.615,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 174.6,
        "Intensity": 0.855,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 174.7,
        "Intensity": 2.984,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 174.94,
        "Intensity": 9.5,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 174.954,
        "Intensity": 58.606,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 175.361,
        "Intensity": 7.478,
        "Nuclide": "Sc-48 (B- 43.67 H)"
    },
    {
        "E(keV)": 175.43,
        "Intensity": 1.757,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 175.7,
        "Intensity": 0.002805,
        "Nuclide": "Es-254m (A 39.3 H)"
    },
    {
        "E(keV)": 176.3,
        "Intensity": 4.08,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 176.314,
        "Intensity": 6.887,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 176.6,
        "Intensity": 17.7,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 176.602,
        "Intensity": 9.97,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 176.653,
        "Intensity": 0.01076,
        "Nuclide": "Lu-174 (EC 3.31 Y)"
    },
    {
        "E(keV)": 176.653,
        "Intensity": 0.47,
        "Nuclide": "Lu-174m (EC 142 D)"
    },
    {
        "E(keV)": 176.98,
        "Intensity": 0.0043,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 177.036,
        "Intensity": 0.268,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 177.16,
        "Intensity": 3.825,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 177.21402,
        "Intensity": 22.064,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 177.214,
        "Intensity": 0.27,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 177.3,
        "Intensity": 0.0561,
        "Nuclide": "Es-254m (A 39.3 H)"
    },
    {
        "E(keV)": 177.6,
        "Intensity": 2.4,
        "Nuclide": "Es-251 (EC 33 H)"
    },
    {
        "E(keV)": 178.58,
        "Intensity": 0.0184,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 178.96,
        "Intensity": 1.113,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 179.365,
        "Intensity": 1.392,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 179.3945,
        "Intensity": 3.082,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 179.4,
        "Intensity": 8.682,
        "Nuclide": "Fm-257 (A 100.5 D)"
    },
    {
        "E(keV)": 179.54,
        "Intensity": 0.151,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 179.636,
        "Intensity": 0.501,
        "Nuclide": "Rh-101m (EC 4.34 D)"
    },
    {
        "E(keV)": 179.94,
        "Intensity": 9.7,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 180.03,
        "Intensity": 0.182,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 180.08,
        "Intensity": 7.379,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 180.277,
        "Intensity": 0.482,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 180.31,
        "Intensity": 50.05,
        "Nuclide": "Au-198m (IT 2.27 D)"
    },
    {
        "E(keV)": 180.4,
        "Intensity": 0.002226,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 180.9,
        "Intensity": 0.063,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 181.068,
        "Intensity": 5.992,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 181.1,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 181.1,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 181.52,
        "Intensity": 2.754,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 181.525,
        "Intensity": 21.066,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 181.8,
        "Intensity": 7.325e-06,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 181.81,
        "Intensity": 0.194,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 181.944,
        "Intensity": 9.878,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 182.2,
        "Intensity": 5.246e-06,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 182.25,
        "Intensity": 0.85,
        "Nuclide": "Te-131m (IT 30 H)"
    },
    {
        "E(keV)": 182.5,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 182.61,
        "Intensity": 0.34,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 183.44,
        "Intensity": 0.945,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 183.5,
        "Intensity": 4.75,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 183.83,
        "Intensity": 0.0009756,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 183.977,
        "Intensity": 16.102,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 184.11,
        "Intensity": 0.146,
        "Nuclide": "Rh-101m (EC 4.34 D)"
    },
    {
        "E(keV)": 184.22,
        "Intensity": 0.05928,
        "Nuclide": "Rh-101 (EC 3.3 Y)"
    },
    {
        "E(keV)": 184.295,
        "Intensity": 18.104,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 184.4,
        "Intensity": 0.002,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 184.41,
        "Intensity": 72.6,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 184.577,
        "Intensity": 48.7,
        "Nuclide": "Cu-67 (B- 61.83 H)"
    },
    {
        "E(keV)": 184.577,
        "Intensity": 21.16,
        "Nuclide": "Ga-67 (EC 3.2612 D)"
    },
    {
        "E(keV)": 184.6,
        "Intensity": 8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 184.68,
        "Intensity": 0.00424,
        "Nuclide": "Eu-154 (EC 8.593 Y)"
    },
    {
        "E(keV)": 184.8,
        "Intensity": 0.0132,
        "Nuclide": "Th-234 (B- 24.10 D)"
    },
    {
        "E(keV)": 185.0,
        "Intensity": 0.00462,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 185.0,
        "Intensity": 5.6e-07,
        "Nuclide": "Np-235 (A 396.2 D)"
    },
    {
        "E(keV)": 185.1,
        "Intensity": 126,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 185.2,
        "Intensity": 2.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 185.2,
        "Intensity": 3.267,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 185.4,
        "Intensity": 15.246,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 185.6,
        "Intensity": 0.809,
        "Nuclide": "Ac-226 (EC 29.37 H)"
    },
    {
        "E(keV)": 185.6,
        "Intensity": 3.42,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 185.715,
        "Intensity": 57.2,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 185.8,
        "Intensity": 0.01045,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 185.89,
        "Intensity": 1.886,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 185.89,
        "Intensity": 0.181,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 186.053,
        "Intensity": 0.008787,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 186.211,
        "Intensity": 3.59,
        "Nuclide": "Ra-226 (A 1600 Y)"
    },
    {
        "E(keV)": 186.68,
        "Intensity": 51.155,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 187.0,
        "Intensity": 0.03772,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 187.0,
        "Intensity": 0.03772,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 187.013,
        "Intensity": 0.02184,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 187.285,
        "Intensity": 0.359,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 187.59,
        "Intensity": 20.157,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 187.69,
        "Intensity": 0.456,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 187.8,
        "Intensity": 7,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 188.0,
        "Intensity": 0.54,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 188.01,
        "Intensity": 0.0002343,
        "Nuclide": "Re-184m (IT 169 D)"
    },
    {
        "E(keV)": 188.55,
        "Intensity": 0.498,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 189.0,
        "Intensity": 0.0475,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 189.0,
        "Intensity": 0.0009,
        "Nuclide": "Fe-59 (B- 44.503 D)"
    },
    {
        "E(keV)": 189.5,
        "Intensity": 3.861,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 189.63,
        "Intensity": 1.099,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 189.82,
        "Intensity": 0.193,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 190.27,
        "Intensity": 15.56,
        "Nuclide": "In-114m (IT 49.51 D)"
    },
    {
        "E(keV)": 191.0,
        "Intensity": 3.108e-05,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 191.2137,
        "Intensity": 22.635,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 191.364,
        "Intensity": 0.632,
        "Nuclide": "Hg-197 (EC 64.14 H)"
    },
    {
        "E(keV)": 191.38,
        "Intensity": 0.591,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 191.4,
        "Intensity": 0.029,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 191.5,
        "Intensity": 9.368,
        "Nuclide": "Zn-72 (B- 46.5 H)"
    },
    {
        "E(keV)": 192.1,
        "Intensity": 14,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 192.2,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 192.349,
        "Intensity": 3.08,
        "Nuclide": "Fe-59 (B- 44.503 D)"
    },
    {
        "E(keV)": 192.66,
        "Intensity": 21.429,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 192.7,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 193.157,
        "Intensity": 0.04047,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 193.5,
        "Intensity": 0.05168,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 193.509,
        "Intensity": 4.412,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 193.7,
        "Intensity": 1.72,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 193.7,
        "Intensity": 5.3,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 194.94,
        "Intensity": 0.63,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 194.95,
        "Intensity": 0.184,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 195.0,
        "Intensity": 0.0009548,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 195.0,
        "Intensity": 0.0012,
        "Nuclide": "Bk-245 (A 4.94 D)"
    },
    {
        "E(keV)": 195.05,
        "Intensity": 19.35,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 195.5601,
        "Intensity": 0.842,
        "Nuclide": "Lu-177m (IT 160.4 D)"
    },
    {
        "E(keV)": 195.78,
        "Intensity": 0.164,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 196.2,
        "Intensity": 0.02871,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 196.49,
        "Intensity": 0.02871,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 196.56,
        "Intensity": 4.59,
        "Nuclide": "Xe-129m (IT 8.88 D)"
    },
    {
        "E(keV)": 196.64,
        "Intensity": 0.204,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 196.85,
        "Intensity": 3.336,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 197.0352,
        "Intensity": 5.183,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 197.1,
        "Intensity": 36,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 197.299,
        "Intensity": 26.451,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 197.299,
        "Intensity": 3.42e-07,
        "Nuclide": "Pm-147 (B- 2.6234 Y)"
    },
    {
        "E(keV)": 197.3,
        "Intensity": 87,
        "Nuclide": "Sb-120 (EC 5.76 D)"
    },
    {
        "E(keV)": 197.33,
        "Intensity": 0.265,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 197.5,
        "Intensity": 12,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 197.8,
        "Intensity": 0.06047,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 197.891,
        "Intensity": 0.01362,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 197.95788,
        "Intensity": 35.644,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 198.0,
        "Intensity": 0.158,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 198.0,
        "Intensity": 10,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 198.01,
        "Intensity": 73.186,
        "Nuclide": "Rh-101 (EC 3.3 Y)"
    },
    {
        "E(keV)": 198.251,
        "Intensity": 54.366,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 198.6,
        "Intensity": 0.429,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 198.606,
        "Intensity": 1.47,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 198.61,
        "Intensity": 6.684e-05,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 199.19,
        "Intensity": 40.92,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 199.2,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 199.46,
        "Intensity": 0.008616,
        "Nuclide": "Au-195 (EC 186.098 D)"
    },
    {
        "E(keV)": 200.38,
        "Intensity": 0.785,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 200.4,
        "Intensity": 1.205,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 200.47,
        "Intensity": 0.001065,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 200.58,
        "Intensity": 0.0536,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 200.63,
        "Intensity": 7.696,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 200.97,
        "Intensity": 3.9e-06,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 201.3112,
        "Intensity": 0.463,
        "Nuclide": "Ir-192 (EC 73.827 D)"
    },
    {
        "E(keV)": 201.83,
        "Intensity": 77.969,
        "Nuclide": "Lu-176 (B- 4.00E10 Y)"
    },
    {
        "E(keV)": 202.11,
        "Intensity": 1.08,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 202.6,
        "Intensity": 43,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 202.724,
        "Intensity": 1.031,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 202.86,
        "Intensity": 68.31,
        "Nuclide": "Xe-127 (EC 36.4 D)"
    },
    {
        "E(keV)": 203.4,
        "Intensity": 21,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 203.4,
        "Intensity": 21,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 203.433,
        "Intensity": 5.142,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 203.55,
        "Intensity": 0.000569,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 204.0,
        "Intensity": 0.17,
        "Nuclide": "Cf-254 (SF 60.5 D)"
    },
    {
        "E(keV)": 204.0,
        "Intensity": 0.605,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 204.1,
        "Intensity": 40.81,
        "Nuclide": "Au-198m (IT 2.27 D)"
    },
    {
        "E(keV)": 204.1052,
        "Intensity": 13.849,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 204.117,
        "Intensity": 62.464,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 204.12,
        "Intensity": 0.02795,
        "Nuclide": "Nb-95 (B- 34.975 D)"
    },
    {
        "E(keV)": 204.12,
        "Intensity": 2.33,
        "Nuclide": "Nb-95m (B- 86.6 H)"
    },
    {
        "E(keV)": 204.138,
        "Intensity": 0.319,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 204.5,
        "Intensity": 4,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 205.0,
        "Intensity": 5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 205.05,
        "Intensity": 2.93e-05,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 205.1,
        "Intensity": 5.151e-06,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 205.311,
        "Intensity": 5.01,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 205.7943,
        "Intensity": 3.269,
        "Nuclide": "Ir-192 (EC 73.827 D)"
    },
    {
        "E(keV)": 205.879,
        "Intensity": 2.714,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 205.93,
        "Intensity": 0.01964,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 206.37,
        "Intensity": 0.08011,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 207.1,
        "Intensity": 0.361,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 207.4,
        "Intensity": 0.0396,
        "Nuclide": "Bk-245 (A 4.94 D)"
    },
    {
        "E(keV)": 207.8,
        "Intensity": 41.278,
        "Nuclide": "Tm-167 (EC 9.25 D)"
    },
    {
        "E(keV)": 207.86,
        "Intensity": 0.00804,
        "Nuclide": "W-188 (B- 69.4 D)"
    },
    {
        "E(keV)": 208.0,
        "Intensity": 21.2,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 208.01,
        "Intensity": 0.000791,
        "Nuclide": "Am-241 (A 432.2 Y)"
    },
    {
        "E(keV)": 208.077,
        "Intensity": 0.249,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 208.20597,
        "Intensity": 8.72,
        "Nuclide": "Au-199 (B- 3.139 D)"
    },
    {
        "E(keV)": 208.283,
        "Intensity": 0.01204,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 208.3664,
        "Intensity": 57.684,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 208.3664,
        "Intensity": 11,
        "Nuclide": "Lu-177 (B- 6.73 D)"
    },
    {
        "E(keV)": 208.4,
        "Intensity": 0.939,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 208.48,
        "Intensity": 0.723,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 208.8107,
        "Intensity": 2.954,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 208.951,
        "Intensity": 0.115,
        "Nuclide": "Cu-67 (B- 61.83 H)"
    },
    {
        "E(keV)": 208.951,
        "Intensity": 2.396,
        "Nuclide": "Ga-67 (EC 3.2612 D)"
    },
    {
        "E(keV)": 209.0,
        "Intensity": 1.733,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 209.5,
        "Intensity": 1.062e-05,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 209.753,
        "Intensity": 3.292,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 209.753,
        "Intensity": 3.42,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 209.8658,
        "Intensity": 4.476,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 210.0,
        "Intensity": 1.5e-05,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 210.27,
        "Intensity": 1.368,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 210.65,
        "Intensity": 1.107,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 210.7,
        "Intensity": 0.009616,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 210.8,
        "Intensity": 4e-05,
        "Nuclide": "Dy-159 (EC 144.4 D)"
    },
    {
        "E(keV)": 210.853,
        "Intensity": 2.77,
        "Nuclide": "Th-229 (A 7340 Y)"
    },
    {
        "E(keV)": 211.1,
        "Intensity": 3.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 211.35,
        "Intensity": 0.03887,
        "Nuclide": "Pt-195m (IT 4.02 D)"
    },
    {
        "E(keV)": 211.36,
        "Intensity": 0.01091,
        "Nuclide": "Au-195 (EC 186.098 D)"
    },
    {
        "E(keV)": 211.8,
        "Intensity": 0.0957,
        "Nuclide": "Es-254m (A 39.3 H)"
    },
    {
        "E(keV)": 212.0,
        "Intensity": 31.084,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 212.189,
        "Intensity": 81.423,
        "Nuclide": "Te-121m (IT 154 D)"
    },
    {
        "E(keV)": 212.29,
        "Intensity": 0.155,
        "Nuclide": "Np-237 (A 2.14E+6 Y)"
    },
    {
        "E(keV)": 212.3,
        "Intensity": 0.0294,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 212.46,
        "Intensity": 2.9e-05,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 212.6,
        "Intensity": 1.6,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 213.434,
        "Intensity": 81.396,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 214.0,
        "Intensity": 0.2,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 214.4339,
        "Intensity": 6.593,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 214.89,
        "Intensity": 77,
        "Nuclide": "Au-198m (IT 2.27 D)"
    },
    {
        "E(keV)": 215.1,
        "Intensity": 2.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 215.326,
        "Intensity": 2.777,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 215.47,
        "Intensity": 0.06963,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 215.6464,
        "Intensity": 4.018,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 215.7,
        "Intensity": 85.561,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 215.983,
        "Intensity": 0.254,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 216.078,
        "Intensity": 19.665,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 216.547,
        "Intensity": 9.426,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 216.55,
        "Intensity": 0.113,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 216.668,
        "Intensity": 64.647,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 216.68,
        "Intensity": 5.5,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 216.68,
        "Intensity": 0.518,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 216.9,
        "Intensity": 0.316,
        "Nuclide": "Ac-225 (A 10.0 D)"
    },
    {
        "E(keV)": 217.0,
        "Intensity": 10.32,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 217.04,
        "Intensity": 8.991,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 217.07,
        "Intensity": 2.215,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 217.159,
        "Intensity": 0.0032,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 217.2,
        "Intensity": 35,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 217.9,
        "Intensity": 0.806,
        "Nuclide": "U-231 (EC 4.2 D)"
    },
    {
        "E(keV)": 218.1039,
        "Intensity": 3.282,
        "Nuclide": "Lu-177m (IT 160.4 D)"
    },
    {
        "E(keV)": 218.221,
        "Intensity": 0.933,
        "Nuclide": "Tb-158 (B- 180 Y)"
    },
    {
        "E(keV)": 218.66,
        "Intensity": 0.04248,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 218.7,
        "Intensity": 67,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 218.859,
        "Intensity": 3.371,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 219.13,
        "Intensity": 0.277,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 219.4,
        "Intensity": 4.537,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 219.4,
        "Intensity": 0.53,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 219.5,
        "Intensity": 0.088,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 219.65,
        "Intensity": 0.903,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 220.7,
        "Intensity": 0.503,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 220.8,
        "Intensity": 51,
        "Nuclide": "Cf,248CM-252 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 221.0,
        "Intensity": 5e-05,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 221.38,
        "Intensity": 0.12,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 221.48,
        "Intensity": 2.264,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 221.8,
        "Intensity": 0.0212,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 222.07,
        "Intensity": 8.393,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 222.1096,
        "Intensity": 7.486,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 222.5,
        "Intensity": 0.21,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 222.7,
        "Intensity": 49,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 223.0,
        "Intensity": 4.2,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 223.163,
        "Intensity": 0.142,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 223.234,
        "Intensity": 0.00012,
        "Nuclide": "Xe-133 (B- 5.243 D)"
    },
    {
        "E(keV)": 223.2373,
        "Intensity": 0.465,
        "Nuclide": "Ba-133 (EC 10.52 Y)"
    },
    {
        "E(keV)": 223.6,
        "Intensity": 30,
        "Nuclide": "Cf,248CM-252 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 223.75,
        "Intensity": 23.5,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 223.8,
        "Intensity": 0.367,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 223.81,
        "Intensity": 3.648,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 223.9,
        "Intensity": 0.00024,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 224.0,
        "Intensity": 8.7,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 224.4,
        "Intensity": 2.666,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 224.9,
        "Intensity": 80,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 226.0,
        "Intensity": 3.6e-06,
        "Nuclide": "Dy-159 (EC 144.4 D)"
    },
    {
        "E(keV)": 226.38,
        "Intensity": 0.28,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 226.748,
        "Intensity": 1.475,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 227.0,
        "Intensity": 6.3,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 227.09,
        "Intensity": 0.221,
        "Nuclide": "W-188 (B- 69.4 D)"
    },
    {
        "E(keV)": 227.1,
        "Intensity": 8.649,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 227.83,
        "Intensity": 0.51,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 228.0,
        "Intensity": 0.02736,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 228.16,
        "Intensity": 88,
        "Nuclide": "Te-132 (B- 3.204 D)"
    },
    {
        "E(keV)": 228.183,
        "Intensity": 10.76,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 228.184,
        "Intensity": 10.575,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 228.4838,
        "Intensity": 36.971,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 228.5,
        "Intensity": 1.83e-05,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 228.56,
        "Intensity": 0.0003314,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 229.3,
        "Intensity": 152,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 229.32,
        "Intensity": 64.05,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 229.32,
        "Intensity": 25.432,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 229.322,
        "Intensity": 3.63,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 229.5,
        "Intensity": 0.0396,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 229.5,
        "Intensity": 0.106,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 229.6,
        "Intensity": 0.712,
        "Nuclide": "Hf-175 (EC 70 D)"
    },
    {
        "E(keV)": 230.0,
        "Intensity": 26.892,
        "Nuclide": "Ac-226 (B- 29.37 H)"
    },
    {
        "E(keV)": 230.37,
        "Intensity": 0.122,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 230.4,
        "Intensity": 0.0003999,
        "Nuclide": "Co-57 (EC 271.74 D)"
    },
    {
        "E(keV)": 230.7,
        "Intensity": 23,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 230.9,
        "Intensity": 0.02432,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 231.1,
        "Intensity": 0.036,
        "Nuclide": "Cm-247 (A 1.56E+7 Y)"
    },
    {
        "E(keV)": 231.44,
        "Intensity": 0.00088,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 231.443,
        "Intensity": 0.74,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 231.55,
        "Intensity": 2.054,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 232.0,
        "Intensity": 4.08,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 232.4,
        "Intensity": 27,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 232.6,
        "Intensity": 0.0011,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 232.7,
        "Intensity": 0.431,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 232.7,
        "Intensity": 0.0152,
        "Nuclide": "Cm-245 (A 8500 Y)"
    },
    {
        "E(keV)": 232.75,
        "Intensity": 0.08,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 232.8,
        "Intensity": 30.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 233.0,
        "Intensity": 0.008,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 233.221,
        "Intensity": 10,
        "Nuclide": "Xe-133m (IT 2.19 D)"
    },
    {
        "E(keV)": 233.59,
        "Intensity": 0.301,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 233.6,
        "Intensity": 10,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 233.605,
        "Intensity": 0.56,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 233.74,
        "Intensity": 0.167,
        "Nuclide": "Rh-101m (EC 4.34 D)"
    },
    {
        "E(keV)": 233.8608,
        "Intensity": 5.576,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 234.157,
        "Intensity": 0.428,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 234.79,
        "Intensity": 0.281,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 234.8,
        "Intensity": 7,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 234.8,
        "Intensity": 4.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 235.0,
        "Intensity": 8.383e-06,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 235.3,
        "Intensity": 0.04303,
        "Nuclide": "Ac-226 (B- 29.37 H)"
    },
    {
        "E(keV)": 235.3,
        "Intensity": 0.0117,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 235.69,
        "Intensity": 24.902,
        "Nuclide": "Nb-95m (IT 86.6 H)"
    },
    {
        "E(keV)": 235.69,
        "Intensity": 0.294,
        "Nuclide": "Zr-95 (B- 64.02 D)"
    },
    {
        "E(keV)": 235.971,
        "Intensity": 12.3,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 236.0,
        "Intensity": 0.201,
        "Nuclide": "U-231 (EC 4.2 D)"
    },
    {
        "E(keV)": 236.48,
        "Intensity": 18.725,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 236.6,
        "Intensity": 100,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 237.19,
        "Intensity": 0.0005086,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 237.431,
        "Intensity": 9.316,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 237.8,
        "Intensity": 0.09,
        "Nuclide": "Th-231 (B- 25.52 H)"
    },
    {
        "E(keV)": 238.27,
        "Intensity": 0.19,
        "Nuclide": "Rh-101m (EC 4.34 D)"
    },
    {
        "E(keV)": 238.97,
        "Intensity": 0.08739,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 238.98,
        "Intensity": 22.953,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 239.011,
        "Intensity": 1.59,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 239.5,
        "Intensity": 0.05438,
        "Nuclide": "Pt-195m (IT 4.02 D)"
    },
    {
        "E(keV)": 239.629,
        "Intensity": 2.411,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 239.65,
        "Intensity": 0.01312,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 239.9,
        "Intensity": 9.405,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 240.09,
        "Intensity": 3.825,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 240.8,
        "Intensity": 3.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 240.86,
        "Intensity": 0.208,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 240.87,
        "Intensity": 0.075,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 240.93,
        "Intensity": 7.736,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 240.986,
        "Intensity": 4.1,
        "Nuclide": "Ra-224 (A 3.66 D)"
    },
    {
        "E(keV)": 241.0,
        "Intensity": 10.977,
        "Nuclide": "Fm-257 (A 100.5 D)"
    },
    {
        "E(keV)": 241.0,
        "Intensity": 16,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 241.7,
        "Intensity": 0.001628,
        "Nuclide": "Ac-227 (A 21.773 Y)"
    },
    {
        "E(keV)": 241.88,
        "Intensity": 4.782e-07,
        "Nuclide": "Pd-103 (EC 16.991 D)"
    },
    {
        "E(keV)": 241.88,
        "Intensity": 0.01802,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 241.93,
        "Intensity": 0.414,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 242.0,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 242.738,
        "Intensity": 0.0272,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 242.917,
        "Intensity": 35.863,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 243.29,
        "Intensity": 5.636,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 244.1,
        "Intensity": 4.3,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 244.2649,
        "Intensity": 8.496,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 244.2663,
        "Intensity": 0.408,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 244.6975,
        "Intensity": 7.598,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 245.08,
        "Intensity": 3.52,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 245.08,
        "Intensity": 6.023,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 245.345,
        "Intensity": 0.00362,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 245.4,
        "Intensity": 94.009,
        "Nuclide": "In-111 (EC 2.8047 D)"
    },
    {
        "E(keV)": 245.4,
        "Intensity": 1.329,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 246.0587,
        "Intensity": 26.8,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 246.062,
        "Intensity": 1.311,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 246.5,
        "Intensity": 23,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 246.885,
        "Intensity": 0.632,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 247.1,
        "Intensity": 0.32,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 247.5,
        "Intensity": 0.0003446,
        "Nuclide": "Te-123m (IT 119.7 D)"
    },
    {
        "E(keV)": 247.93,
        "Intensity": 6.915,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 248.2,
        "Intensity": 5.564,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 248.5,
        "Intensity": 0.059,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 248.6,
        "Intensity": 19.8,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 248.6,
        "Intensity": 80,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 249.0,
        "Intensity": 0.025,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 249.432,
        "Intensity": 2.814,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 249.55,
        "Intensity": 2.331,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 249.6741,
        "Intensity": 6.142,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 249.6741,
        "Intensity": 0.212,
        "Nuclide": "Lu-177 (B- 6.73 D)"
    },
    {
        "E(keV)": 249.7,
        "Intensity": 0.02103,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 249.7,
        "Intensity": 0.03098,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 249.77,
        "Intensity": 2.961,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 249.805,
        "Intensity": 0.394,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 250.0,
        "Intensity": 74.25,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 250.1,
        "Intensity": 17,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 250.2,
        "Intensity": 0.00224,
        "Nuclide": "Tm-167 (EC 9.25 D)"
    },
    {
        "E(keV)": 250.4,
        "Intensity": 14.25,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 250.4,
        "Intensity": 0.0384,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 250.5,
        "Intensity": 14.25,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 251.0,
        "Intensity": 2.88,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 251.1,
        "Intensity": 58,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 251.1,
        "Intensity": 0.01701,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 251.2,
        "Intensity": 9.8e-06,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 251.474,
        "Intensity": 0.08384,
        "Nuclide": "Yb-175 (B- 4.185 D)"
    },
    {
        "E(keV)": 251.51,
        "Intensity": 0.01084,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 251.62,
        "Intensity": 0.217,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 252.0,
        "Intensity": 9e-05,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 252.4,
        "Intensity": 8.501,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 252.8,
        "Intensity": 2.501,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 252.845,
        "Intensity": 10.678,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 252.845,
        "Intensity": 3.011,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 252.85,
        "Intensity": 29.068,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 253.068,
        "Intensity": 0.603,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 253.5,
        "Intensity": 0.971,
        "Nuclide": "Ac-226 (EC 29.37 H)"
    },
    {
        "E(keV)": 253.7,
        "Intensity": 35,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 253.729,
        "Intensity": 0.01111,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 253.8,
        "Intensity": 0.0008484,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 254.0,
        "Intensity": 0.9,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 254.29,
        "Intensity": 11.038,
        "Nuclide": "Ce-137m (IT 34.4 H)"
    },
    {
        "E(keV)": 254.4,
        "Intensity": 0.11,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 254.41,
        "Intensity": 0.11,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 254.566,
        "Intensity": 0.633,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 254.68,
        "Intensity": 0.738,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 255.0,
        "Intensity": 0.2,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 255.134,
        "Intensity": 2.11,
        "Nuclide": "Sn-113 (EC 115.09 D)"
    },
    {
        "E(keV)": 255.4,
        "Intensity": 14,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 255.45,
        "Intensity": 0.02574,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 255.54,
        "Intensity": 0.23,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 255.77,
        "Intensity": 0.112,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 256.0,
        "Intensity": 96,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 256.25,
        "Intensity": 7.011,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 256.4,
        "Intensity": 15,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 256.45,
        "Intensity": 9.41,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 257.38,
        "Intensity": 3.245,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 257.646,
        "Intensity": 16.75,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 258.1,
        "Intensity": 73,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 258.46,
        "Intensity": 0.0001474,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 260.19,
        "Intensity": 0.188,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 260.46,
        "Intensity": 0.04307,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 260.5,
        "Intensity": 1.104,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 260.5,
        "Intensity": 0.675,
        "Nuclide": "Po-209 (A 102 Y)"
    },
    {
        "E(keV)": 260.6,
        "Intensity": 0.209,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 260.736,
        "Intensity": 1.401,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 260.89,
        "Intensity": 0.00092,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 260.896,
        "Intensity": 1.94,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 261.07857,
        "Intensity": 1.707,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 261.29,
        "Intensity": 11.847,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 261.66,
        "Intensity": 0.0001657,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 261.75,
        "Intensity": 30.645,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 262.0,
        "Intensity": 0.2,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 262.27,
        "Intensity": 5.233,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 262.27,
        "Intensity": 0.005,
        "Nuclide": "Ra-226 (A 1600 Y)"
    },
    {
        "E(keV)": 262.54,
        "Intensity": 5.766,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 262.8,
        "Intensity": 0.225,
        "Nuclide": "Po-209 (A 102 Y)"
    },
    {
        "E(keV)": 263.0,
        "Intensity": 9,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 263.23,
        "Intensity": 0.00961,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 263.34,
        "Intensity": 5.39e-05,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 263.7,
        "Intensity": 0.02296,
        "Nuclide": "Cd-113m (IT 14.1 Y)"
    },
    {
        "E(keV)": 263.8,
        "Intensity": 4,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 264.0,
        "Intensity": 0.05,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 264.0752,
        "Intensity": 3.605,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 264.6576,
        "Intensity": 58.562,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 264.9,
        "Intensity": 0.0752,
        "Nuclide": "Tm-167 (EC 9.25 D)"
    },
    {
        "E(keV)": 265.0,
        "Intensity": 30,
        "Nuclide": "Bk-247 (A 1380 Y)"
    },
    {
        "E(keV)": 265.6,
        "Intensity": 50,
        "Nuclide": "Bi-210m (A 3.04E+6 Y)"
    },
    {
        "E(keV)": 265.922,
        "Intensity": 0.402,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 265.922,
        "Intensity": 0.000144,
        "Nuclide": "Bk-245 (A 4.94 D)"
    },
    {
        "E(keV)": 266.0,
        "Intensity": 0.01411,
        "Nuclide": "Pa-230 (B- 17.4 D)"
    },
    {
        "E(keV)": 266.0,
        "Intensity": 0.5,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 266.5,
        "Intensity": 0.00224,
        "Nuclide": "Tm-167 (EC 9.25 D)"
    },
    {
        "E(keV)": 266.543,
        "Intensity": 0.466,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 266.62,
        "Intensity": 0.693,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 266.82,
        "Intensity": 0.271,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 266.985,
        "Intensity": 0.092,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 267.1,
        "Intensity": 1.978,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 267.1,
        "Intensity": 2,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 267.54,
        "Intensity": 0.712,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 267.8,
        "Intensity": 0.03731,
        "Nuclide": "Gd-146 (EC 48.27 D)"
    },
    {
        "E(keV)": 267.92,
        "Intensity": 0.85,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 268.218,
        "Intensity": 16,
        "Nuclide": "Ba-135m (IT 28.7 H)"
    },
    {
        "E(keV)": 268.5,
        "Intensity": 12,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 268.56,
        "Intensity": 0.703,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 268.71,
        "Intensity": 0.03927,
        "Nuclide": "Hg-197 (EC 64.14 H)"
    },
    {
        "E(keV)": 268.71,
        "Intensity": 1.806,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 268.785,
        "Intensity": 3.426,
        "Nuclide": "Lu-177m (IT 160.4 D)"
    },
    {
        "E(keV)": 268.85,
        "Intensity": 11.222,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 269.459,
        "Intensity": 13.7,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 269.5,
        "Intensity": 36.964,
        "Nuclide": "Ni-56 (EC 6.075 D)"
    },
    {
        "E(keV)": 269.7,
        "Intensity": 0.218,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 270.0,
        "Intensity": 0.2,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 270.1,
        "Intensity": 1.282,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 270.2,
        "Intensity": 0.00316,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 270.352,
        "Intensity": 0.212,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 270.405,
        "Intensity": 80,
        "Nuclide": "Hf-182 (B- 9E6 Y)"
    },
    {
        "E(keV)": 270.53,
        "Intensity": 27.638,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 270.85,
        "Intensity": 0.008268,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 271.0,
        "Intensity": 44,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 271.13,
        "Intensity": 86.746,
        "Nuclide": "Sc-44m (IT 58.6 H)"
    },
    {
        "E(keV)": 271.131,
        "Intensity": 0.07293,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 271.4,
        "Intensity": 4.2,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 271.48,
        "Intensity": 0.328,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 271.6,
        "Intensity": 3.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 271.8,
        "Intensity": 2.64,
        "Nuclide": "Fm-253 (A 3.00 D)"
    },
    {
        "E(keV)": 272.105,
        "Intensity": 21.448,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 272.2,
        "Intensity": 0.01207,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 272.321,
        "Intensity": 3.411,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 272.498,
        "Intensity": 0.05776,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 272.87,
        "Intensity": 0.07981,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 272.914,
        "Intensity": 0.55,
        "Nuclide": "Lu-174m (EC 142 D)"
    },
    {
        "E(keV)": 272.93,
        "Intensity": 0.48,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 273.44,
        "Intensity": 14.506,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 273.48,
        "Intensity": 0.802,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 273.646,
        "Intensity": 11.067,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 274.4,
        "Intensity": 75,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 275.21,
        "Intensity": 6.75,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 275.374,
        "Intensity": 0.801,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 275.6,
        "Intensity": 0.0416,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 275.89,
        "Intensity": 0.308,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 275.89,
        "Intensity": 0.542,
        "Nuclide": "Ir-189 (EC 13.2 D)"
    },
    {
        "E(keV)": 275.925,
        "Intensity": 17.798,
        "Nuclide": "Ba-133m (IT 38.9 H)"
    },
    {
        "E(keV)": 275.99,
        "Intensity": 0.297,
        "Nuclide": "Kr-81 (EC 2.29E5 Y)"
    },
    {
        "E(keV)": 276.31,
        "Intensity": 8.647,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 276.3997,
        "Intensity": 7.4,
        "Nuclide": "Ba-133 (EC 10.52 Y)"
    },
    {
        "E(keV)": 276.8,
        "Intensity": 45,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 276.9,
        "Intensity": 4.356,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 276.9,
        "Intensity": 2.039,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 277.089,
        "Intensity": 3.541,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 277.09,
        "Intensity": 0.02883,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 277.403,
        "Intensity": 1.383,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 277.599,
        "Intensity": 13.966,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 277.599,
        "Intensity": 14.38,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 278.0,
        "Intensity": 0.03,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 278.0,
        "Intensity": 3.4,
        "Nuclide": "Cm-247 (A 1.56E+7 Y)"
    },
    {
        "E(keV)": 278.3,
        "Intensity": 0.0005344,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 278.6,
        "Intensity": 2.39,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 278.614,
        "Intensity": 1.317,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 279.1967,
        "Intensity": 82.416,
        "Nuclide": "Pb-203 (EC 51.873 H)"
    },
    {
        "E(keV)": 279.1967,
        "Intensity": 81.46,
        "Nuclide": "Hg-203 (B- 46.612 D)"
    },
    {
        "E(keV)": 279.5,
        "Intensity": 0.27,
        "Nuclide": "U-235 (A 703.8E+6 Y)"
    },
    {
        "E(keV)": 279.5422,
        "Intensity": 24.848,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 280.1,
        "Intensity": 0.166,
        "Nuclide": "Rh-105 (B- 35.36 H)"
    },
    {
        "E(keV)": 280.27,
        "Intensity": 0.009,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 280.3,
        "Intensity": 0.323,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 280.4,
        "Intensity": 0.0009156,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 280.44,
        "Intensity": 31.29,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 280.444,
        "Intensity": 1.244,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 280.459,
        "Intensity": 29.766,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 281.295,
        "Intensity": 0.02248,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 281.3,
        "Intensity": 86,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 281.642,
        "Intensity": 0.05788,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 281.65,
        "Intensity": 2.272,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 281.7873,
        "Intensity": 14.15,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 282.131,
        "Intensity": 0.241,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 282.2,
        "Intensity": 7.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 282.522,
        "Intensity": 3.008,
        "Nuclide": "Yb-175 (B- 4.185 D)"
    },
    {
        "E(keV)": 282.6,
        "Intensity": 39,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 282.8,
        "Intensity": 13.9,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 283.15,
        "Intensity": 0.109,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 283.2668,
        "Intensity": 0.26,
        "Nuclide": "Ir-192 (EC 73.827 D)"
    },
    {
        "E(keV)": 283.3,
        "Intensity": 0.101,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 283.5,
        "Intensity": 0.00058,
        "Nuclide": "Cs-137 (B- 30.04 Y)"
    },
    {
        "E(keV)": 283.69,
        "Intensity": 1.7,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 283.8,
        "Intensity": 0.0624,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 284.15,
        "Intensity": 1.716,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 284.305,
        "Intensity": 6.136,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 285.0,
        "Intensity": 0.01,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 285.0,
        "Intensity": 1.4,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 285.3,
        "Intensity": 10,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 285.362,
        "Intensity": 0.618,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 285.46,
        "Intensity": 0.728,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 285.46,
        "Intensity": 0.79,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 285.95,
        "Intensity": 3.1,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 286.09,
        "Intensity": 0.08988,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 286.122,
        "Intensity": 1.538,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 286.41,
        "Intensity": 23.827,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 286.481,
        "Intensity": 0.01428,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 287.0,
        "Intensity": 11.5,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 287.2,
        "Intensity": 100,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 287.5,
        "Intensity": 2,
        "Nuclide": "Cm-247 (A 1.56E+7 Y)"
    },
    {
        "E(keV)": 288.0,
        "Intensity": 6.407e-05,
        "Nuclide": "Ba-133m (IT 38.9 H)"
    },
    {
        "E(keV)": 288.11,
        "Intensity": 12.505,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 288.18,
        "Intensity": 0.158,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 288.3,
        "Intensity": 0.548,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 289.4,
        "Intensity": 112,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 290.0,
        "Intensity": 9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 290.2,
        "Intensity": 6,
        "Nuclide": "Cf,248CM-252 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 290.2,
        "Intensity": 0.000137,
        "Nuclide": "Dy-159 (EC 144.4 D)"
    },
    {
        "E(keV)": 290.64,
        "Intensity": 0.111,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 290.66,
        "Intensity": 0.0138,
        "Nuclide": "Dy-166 (B- 81.6 H)"
    },
    {
        "E(keV)": 290.669,
        "Intensity": 0.402,
        "Nuclide": "W-188 (B- 69.4 D)"
    },
    {
        "E(keV)": 290.8,
        "Intensity": 2.024,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 291.0,
        "Intensity": 0.4,
        "Nuclide": "Cf-251 (A 898 Y)"
    },
    {
        "E(keV)": 291.354,
        "Intensity": 0.00537,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 291.6,
        "Intensity": 6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 291.7231,
        "Intensity": 3.725,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 291.7282,
        "Intensity": 3.057,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 291.9,
        "Intensity": 0.001351,
        "Nuclide": "Po-208 (EC 2.898 Y)"
    },
    {
        "E(keV)": 292.401,
        "Intensity": 0.05814,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 292.7,
        "Intensity": 0.0062,
        "Nuclide": "Ra-224 (A 3.66 D)"
    },
    {
        "E(keV)": 292.7,
        "Intensity": 0.005733,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 293.1,
        "Intensity": 1.071,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 293.266,
        "Intensity": 42.8,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 293.58,
        "Intensity": 10.394,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 293.7,
        "Intensity": 1.71,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 294.264,
        "Intensity": 0.05409,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 294.75,
        "Intensity": 6.45,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 294.98,
        "Intensity": 0.002801,
        "Nuclide": "Pd-103 (EC 16.991 D)"
    },
    {
        "E(keV)": 294.98,
        "Intensity": 0.303,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 295.01,
        "Intensity": 0.596,
        "Nuclide": "Rh-101 (EC 3.3 Y)"
    },
    {
        "E(keV)": 295.01,
        "Intensity": 0.02175,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 295.7,
        "Intensity": 1.16,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 295.72,
        "Intensity": 0.136,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 295.9392,
        "Intensity": 0.448,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 295.9565,
        "Intensity": 28.72,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 296.1,
        "Intensity": 100,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 296.119,
        "Intensity": 3.916,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 296.49,
        "Intensity": 4.464,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 296.812,
        "Intensity": 9.692,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 296.9,
        "Intensity": 5.3e-05,
        "Nuclide": "Re-186 (B- 3.7183 D)"
    },
    {
        "E(keV)": 297.23,
        "Intensity": 4.132,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 297.3,
        "Intensity": 4.482,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 297.369,
        "Intensity": 12.839,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 298.5,
        "Intensity": 0.035,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 298.58,
        "Intensity": 26.127,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 298.634,
        "Intensity": 30.372,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 298.7,
        "Intensity": 6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 298.7,
        "Intensity": 6,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 298.8,
        "Intensity": 3.12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 298.83,
        "Intensity": 0.186,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 298.89,
        "Intensity": 0.0006611,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 299.34,
        "Intensity": 0.03,
        "Nuclide": "Pu-246 (B- 10.84 D)"
    },
    {
        "E(keV)": 299.53,
        "Intensity": 1.433,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 299.8,
        "Intensity": 1.575,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 300.0,
        "Intensity": 2.325,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 300.07,
        "Intensity": 2.465,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 300.2,
        "Intensity": 2.772,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 300.219,
        "Intensity": 0.797,
        "Nuclide": "Cu-67 (B- 61.83 H)"
    },
    {
        "E(keV)": 300.219,
        "Intensity": 16.769,
        "Nuclide": "Ga-67 (EC 3.2612 D)"
    },
    {
        "E(keV)": 300.34,
        "Intensity": 6.62,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 300.762,
        "Intensity": 3.732,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 300.884,
        "Intensity": 0.08815,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 301.7,
        "Intensity": 22,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 301.7,
        "Intensity": 0.179,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 302.1,
        "Intensity": 23,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 302.3,
        "Intensity": 18,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 302.65,
        "Intensity": 0.68,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 302.65,
        "Intensity": 2.193,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 302.851,
        "Intensity": 18.935,
        "Nuclide": "Ba-133 (EC 10.52 Y)"
    },
    {
        "E(keV)": 302.853,
        "Intensity": 0.0048,
        "Nuclide": "Xe-133 (B- 5.243 D)"
    },
    {
        "E(keV)": 302.99,
        "Intensity": 1.666e-05,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 303.3,
        "Intensity": 19.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 303.52,
        "Intensity": 0.926,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 303.59,
        "Intensity": 0.03774,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 303.74,
        "Intensity": 0.0864,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 303.76,
        "Intensity": 1.171,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 303.9236,
        "Intensity": 1.309,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 304.0,
        "Intensity": 0.07,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 304.519,
        "Intensity": 1.23,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 304.7,
        "Intensity": 27.5,
        "Nuclide": "Bi-210m (A 3.04E+6 Y)"
    },
    {
        "E(keV)": 304.849,
        "Intensity": 4.293,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 305.4,
        "Intensity": 2.655e-05,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 305.5,
        "Intensity": 1.08e-06,
        "Nuclide": "Dy-159 (EC 144.4 D)"
    },
    {
        "E(keV)": 306.1,
        "Intensity": 5.1,
        "Nuclide": "Rh-105 (B- 35.36 H)"
    },
    {
        "E(keV)": 306.25,
        "Intensity": 0.909,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 306.47,
        "Intensity": 2.429,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 306.5,
        "Intensity": 32,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 306.84,
        "Intensity": 93.6,
        "Nuclide": "Lu-176 (B- 4.00E10 Y)"
    },
    {
        "E(keV)": 306.857,
        "Intensity": 75.835,
        "Nuclide": "Rh-101m (EC 4.34 D)"
    },
    {
        "E(keV)": 306.9,
        "Intensity": 1.088,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 307.1,
        "Intensity": 9.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 307.5,
        "Intensity": 1.042,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 307.5,
        "Intensity": 15,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 307.5,
        "Intensity": 3.19e-06,
        "Nuclide": "Bk-249 (A 320 D)"
    },
    {
        "E(keV)": 307.5,
        "Intensity": 15,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 307.52,
        "Intensity": 0.499,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 307.73757,
        "Intensity": 10.009,
        "Nuclide": "Yb-169 (EC 32.026 D)"
    },
    {
        "E(keV)": 307.9,
        "Intensity": 5.952,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 308.45507,
        "Intensity": 29.68,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 309.5,
        "Intensity": 0.01882,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 309.96,
        "Intensity": 4.273,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 310.0,
        "Intensity": 2.76,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 311.0,
        "Intensity": 12,
        "Nuclide": "Cf,248CM-252 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 311.4,
        "Intensity": 0.01327,
        "Nuclide": "Rh-101m (EC 4.34 D)"
    },
    {
        "E(keV)": 311.56,
        "Intensity": 4.243,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 311.63,
        "Intensity": 3.9,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 312.17,
        "Intensity": 38.6,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 312.5,
        "Intensity": 93,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 313.0149,
        "Intensity": 3.323,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 313.0204,
        "Intensity": 0.415,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 313.27,
        "Intensity": 4.154,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 313.34,
        "Intensity": 0.0002545,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 314.1,
        "Intensity": 344,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 314.27,
        "Intensity": 2.422,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 314.3,
        "Intensity": 0.0004234,
        "Nuclide": "Sn-117m (IT 13.60 D)"
    },
    {
        "E(keV)": 314.4,
        "Intensity": 14.3,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 314.6,
        "Intensity": 11,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 314.8,
        "Intensity": 0.09408,
        "Nuclide": "Pa-230 (B- 17.4 D)"
    },
    {
        "E(keV)": 315.88,
        "Intensity": 0.01796,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 315.88,
        "Intensity": 1.6,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 315.93,
        "Intensity": 20.212,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 316.0,
        "Intensity": 0.15,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 316.201,
        "Intensity": 0.00248,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 316.5,
        "Intensity": 5.3,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 316.5,
        "Intensity": 1.39,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 316.50618,
        "Intensity": 82.711,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 316.9,
        "Intensity": 4.3,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 317.16,
        "Intensity": 0.03191,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 317.16,
        "Intensity": 0.00776,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 317.72,
        "Intensity": 1.503e-05,
        "Nuclide": "Pd-103 (EC 16.991 D)"
    },
    {
        "E(keV)": 317.77,
        "Intensity": 0.01911,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 318.008,
        "Intensity": 5.75,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 318.088,
        "Intensity": 0.07761,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 318.18,
        "Intensity": 2.439,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 318.6,
        "Intensity": 176,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 318.63,
        "Intensity": 1.184,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 318.9,
        "Intensity": 19.1,
        "Nuclide": "Rh-105 (B- 35.36 H)"
    },
    {
        "E(keV)": 318.9,
        "Intensity": 0.175,
        "Nuclide": "Hf-175 (EC 70 D)"
    },
    {
        "E(keV)": 319.0205,
        "Intensity": 10.459,
        "Nuclide": "Lu-177m (IT 160.4 D)"
    },
    {
        "E(keV)": 319.16,
        "Intensity": 4.501,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 319.411,
        "Intensity": 1.953,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 319.911,
        "Intensity": 0.499,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 320.0824,
        "Intensity": 9.92,
        "Nuclide": "Cr-51 (EC 27.7025 D)"
    },
    {
        "E(keV)": 320.541,
        "Intensity": 0.0029,
        "Nuclide": "U-233 (A 1.592E+5 Y)"
    },
    {
        "E(keV)": 320.75,
        "Intensity": 0.0005457,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 321.04,
        "Intensity": 0.418,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 321.24,
        "Intensity": 0.0627,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 321.3,
        "Intensity": 0.02159,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 321.3162,
        "Intensity": 0.219,
        "Nuclide": "Lu-177 (B- 6.73 D)"
    },
    {
        "E(keV)": 321.59,
        "Intensity": 1.276,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 321.7,
        "Intensity": 0.07011,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 321.9,
        "Intensity": 0.29,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 322.45,
        "Intensity": 5.435,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 323.59,
        "Intensity": 0.01563,
        "Nuclide": "Ce-134 (EC 3.16 D)"
    },
    {
        "E(keV)": 323.7,
        "Intensity": 0.00208,
        "Nuclide": "Tm-167 (EC 9.25 D)"
    },
    {
        "E(keV)": 323.871,
        "Intensity": 3.932,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 324.0,
        "Intensity": 2,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 324.49,
        "Intensity": 10.781,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 324.6,
        "Intensity": 26,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 324.6,
        "Intensity": 26,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 324.651,
        "Intensity": 0.02124,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 324.83,
        "Intensity": 0.07213,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 325.23,
        "Intensity": 11.856,
        "Nuclide": "Rh-101 (EC 3.3 Y)"
    },
    {
        "E(keV)": 325.557,
        "Intensity": 94.1,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 325.789,
        "Intensity": 0.274,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 326.0,
        "Intensity": 0.02356,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 326.2,
        "Intensity": 75,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 326.2,
        "Intensity": 0.04944,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 326.4,
        "Intensity": 18,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 326.589,
        "Intensity": 0.0162,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 326.785,
        "Intensity": 2.168,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 327.2,
        "Intensity": 1.74e-05,
        "Nuclide": "Bk-249 (A 320 D)"
    },
    {
        "E(keV)": 327.526,
        "Intensity": 4.009,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 327.6829,
        "Intensity": 18.064,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 327.9,
        "Intensity": 0.002831,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 328.12,
        "Intensity": 0.0006701,
        "Nuclide": "Bi-207 (EC 31.55 Y)"
    },
    {
        "E(keV)": 328.2,
        "Intensity": 52,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 328.31,
        "Intensity": 0.08302,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 328.38,
        "Intensity": 0.0033,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 328.4,
        "Intensity": 0.206,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 328.5,
        "Intensity": 61.144,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 328.5,
        "Intensity": 93,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 328.762,
        "Intensity": 20.32,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 329.17,
        "Intensity": 0.01703,
        "Nuclide": "Ir-192 (EC 73.827 D)"
    },
    {
        "E(keV)": 329.3,
        "Intensity": 0.65,
        "Nuclide": "Bi-210m (A 3.04E+6 Y)"
    },
    {
        "E(keV)": 329.851,
        "Intensity": 2.694,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 330.06,
        "Intensity": 1.396,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 330.7,
        "Intensity": 26,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 330.7,
        "Intensity": 95,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 330.7,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 331.51,
        "Intensity": 4.243,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 332.1,
        "Intensity": 1.407,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 332.11,
        "Intensity": 0.008739,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 332.3,
        "Intensity": 4.921e-05,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 332.36,
        "Intensity": 1.2,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 332.5,
        "Intensity": 1.9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 332.7,
        "Intensity": 102,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 332.7,
        "Intensity": 102,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 332.845,
        "Intensity": 0.000494,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 333.03,
        "Intensity": 22.814,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 333.37,
        "Intensity": 14.586,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 333.4,
        "Intensity": 6.2e-05,
        "Nuclide": "Re-186 (B- 3.7183 D)"
    },
    {
        "E(keV)": 333.8,
        "Intensity": 63.36,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 333.82,
        "Intensity": 16.94,
        "Nuclide": "Au-198m (IT 2.27 D)"
    },
    {
        "E(keV)": 333.971,
        "Intensity": 98.515,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 334.27,
        "Intensity": 9.749,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 334.31,
        "Intensity": 0.02394,
        "Nuclide": "Cm-243 (A 29.1 Y)"
    },
    {
        "E(keV)": 334.31,
        "Intensity": 2.07,
        "Nuclide": "Np-239 (B- 2.3565 D)"
    },
    {
        "E(keV)": 334.321,
        "Intensity": 0.11,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 334.381,
        "Intensity": 1.046,
        "Nuclide": "Th-227 (A 18.72 D)"
    },
    {
        "E(keV)": 334.8,
        "Intensity": 0.27,
        "Nuclide": "Fe-59 (B- 44.503 D)"
    },
    {
        "E(keV)": 335.38,
        "Intensity": 0.0951,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 336.241,
        "Intensity": 45.9,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 336.241,
        "Intensity": 0.00494,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 336.38,
        "Intensity": 6.8e-07,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 338.1,
        "Intensity": 3.704e-05,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 338.281,
        "Intensity": 2.795,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 338.3,
        "Intensity": 10,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 338.4,
        "Intensity": 21,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 338.44,
        "Intensity": 19.175,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 338.8,
        "Intensity": 55,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 339.4,
        "Intensity": 36,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 339.69,
        "Intensity": 0.003699,
        "Nuclide": "Co-57 (EC 271.74 D)"
    },
    {
        "E(keV)": 340.08,
        "Intensity": 22.5,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 340.547,
        "Intensity": 42.175,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 340.67,
        "Intensity": 1.17,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 340.7,
        "Intensity": 1.666e-06,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 340.74,
        "Intensity": 0.181,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 340.81,
        "Intensity": 4.47,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 342.0,
        "Intensity": 0.009,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 342.13,
        "Intensity": 6.68,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 342.9,
        "Intensity": 0.219,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 342.9,
        "Intensity": 9.526,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 343.3,
        "Intensity": 12.6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 343.4,
        "Intensity": 87.562,
        "Nuclide": "Hf-175 (EC 70 D)"
    },
    {
        "E(keV)": 343.5,
        "Intensity": 1.386,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 343.51,
        "Intensity": 0.0552,
        "Nuclide": "Dy-166 (B- 81.6 H)"
    },
    {
        "E(keV)": 343.51,
        "Intensity": 23.851,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 343.7,
        "Intensity": 0.05152,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 344.1,
        "Intensity": 46,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 344.2,
        "Intensity": 0.7,
        "Nuclide": "Bi-210m (A 3.04E+6 Y)"
    },
    {
        "E(keV)": 344.2785,
        "Intensity": 26.52,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 344.52,
        "Intensity": 42.863,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 344.71,
        "Intensity": 0.22,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 344.817,
        "Intensity": 0.627,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 344.9,
        "Intensity": 2.115,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 344.95,
        "Intensity": 0.002958,
        "Nuclide": "Zn-65 (EC 244.26 D)"
    },
    {
        "E(keV)": 345.013,
        "Intensity": 0.000556,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 345.89,
        "Intensity": 0.929,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 345.93,
        "Intensity": 15.118,
        "Nuclide": "Hf-181 (B- 42.39 D)"
    },
    {
        "E(keV)": 346.0,
        "Intensity": 1.3,
        "Nuclide": "Cm-247 (A 1.56E+7 Y)"
    },
    {
        "E(keV)": 346.02,
        "Intensity": 0.691,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 346.5,
        "Intensity": 0.0248,
        "Nuclide": "Tm-167 (EC 9.25 D)"
    },
    {
        "E(keV)": 346.651,
        "Intensity": 25.361,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 346.8,
        "Intensity": 0.178,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 346.93,
        "Intensity": 0.0076,
        "Nuclide": "Co-60 (B- 5.2714 Y)"
    },
    {
        "E(keV)": 346.933,
        "Intensity": 2.905,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 348.0,
        "Intensity": 0.007,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 348.1,
        "Intensity": 0.00095,
        "Nuclide": "Dy-159 (EC 144.4 D)"
    },
    {
        "E(keV)": 348.4,
        "Intensity": 82,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 349.5,
        "Intensity": 3.524,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 349.6,
        "Intensity": 6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 350.0,
        "Intensity": 12.078,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 350.016,
        "Intensity": 0.365,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 350.163,
        "Intensity": 0.269,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 350.5,
        "Intensity": 0.07615,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 350.619,
        "Intensity": 3.231,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 350.774,
        "Intensity": 0.305,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 350.8,
        "Intensity": 74,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 350.95,
        "Intensity": 0.264,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 351.07,
        "Intensity": 10.173,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 351.17,
        "Intensity": 3.682,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 352.0,
        "Intensity": 0.467,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 352.0,
        "Intensity": 1.344,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 352.0,
        "Intensity": 8.55,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 352.2,
        "Intensity": 79,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 352.33,
        "Intensity": 0.002999,
        "Nuclide": "Co-57 (EC 271.74 D)"
    },
    {
        "E(keV)": 353.05,
        "Intensity": 30.16,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 353.3,
        "Intensity": 0.238,
        "Nuclide": "Hf-175 (EC 70 D)"
    },
    {
        "E(keV)": 353.66,
        "Intensity": 0.129,
        "Nuclide": "Gd-151 (EC 124 D)"
    },
    {
        "E(keV)": 353.9904,
        "Intensity": 11.229,
        "Nuclide": "Ta-183 (B- 5.1 D)"
    },
    {
        "E(keV)": 353.9965,
        "Intensity": 0.537,
        "Nuclide": "Re-183 (EC 70.0 D)"
    },
    {
        "E(keV)": 354.06,
        "Intensity": 0.0004993,
        "Nuclide": "Sr-85 (EC 64.84 D)"
    },
    {
        "E(keV)": 354.3,
        "Intensity": 1.387,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 354.5,
        "Intensity": 5.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 355.5,
        "Intensity": 68,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 355.73,
        "Intensity": 86.744,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 356.0134,
        "Intensity": 64.098,
        "Nuclide": "Ba-133 (EC 10.52 Y)"
    },
    {
        "E(keV)": 356.38,
        "Intensity": 13.612,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 356.519,
        "Intensity": 2.779,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 357.12,
        "Intensity": 0.175,
        "Nuclide": "Pa-231 (A 3.276E+4 Y)"
    },
    {
        "E(keV)": 357.3,
        "Intensity": 0.109,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 357.39,
        "Intensity": 0.009373,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 357.45,
        "Intensity": 0.02207,
        "Nuclide": "Pd-103 (EC 16.991 D)"
    },
    {
        "E(keV)": 357.6,
        "Intensity": 0.095,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 358.0,
        "Intensity": 6e-07,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 358.4,
        "Intensity": 0.01634,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 358.9,
        "Intensity": 1.5,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 359.1,
        "Intensity": 0.09574,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 359.5,
        "Intensity": 27.2,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 359.88,
        "Intensity": 6.575,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 361.09,
        "Intensity": 12.7,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 361.81,
        "Intensity": 0.296,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 362.55,
        "Intensity": 39.478,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 362.8,
        "Intensity": 0.0222,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 362.81,
        "Intensity": 2.17e-06,
        "Nuclide": "Kr-85 (B- 10.756 Y)"
    },
    {
        "E(keV)": 362.82,
        "Intensity": 0.0009985,
        "Nuclide": "Sr-85 (EC 64.84 D)"
    },
    {
        "E(keV)": 363.1,
        "Intensity": 34,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 363.34,
        "Intensity": 0.06798,
        "Nuclide": "Cs-132 (EC 6.479 D)"
    },
    {
        "E(keV)": 363.5,
        "Intensity": 5.5e-05,
        "Nuclide": "Dy-159 (EC 144.4 D)"
    },
    {
        "E(keV)": 363.64,
        "Intensity": 0.01571,
        "Nuclide": "Lu-174m (EC 142 D)"
    },
    {
        "E(keV)": 363.95,
        "Intensity": 0.0061,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 364.0,
        "Intensity": 14,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 364.3,
        "Intensity": 2.376,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 364.489,
        "Intensity": 81.7,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 364.87,
        "Intensity": 1.51,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 365.8,
        "Intensity": 0.362,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 365.9,
        "Intensity": 13,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 366.421,
        "Intensity": 1.191,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 366.56,
        "Intensity": 0.07644,
        "Nuclide": "Pa-230 (B- 17.4 D)"
    },
    {
        "E(keV)": 366.8,
        "Intensity": 0.0012,
        "Nuclide": "Co-57 (EC 271.74 D)"
    },
    {
        "E(keV)": 367.36,
        "Intensity": 0.77,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 367.36,
        "Intensity": 1.466,
        "Nuclide": "Tb-155 (EC 5.32 D)"
    },
    {
        "E(keV)": 367.4176,
        "Intensity": 3.15,
        "Nuclide": "Lu-177m (IT 160.4 D)"
    },
    {
        "E(keV)": 367.5,
        "Intensity": 3.1,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 367.7887,
        "Intensity": 0.861,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 367.942,
        "Intensity": 86.718,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 368.1,
        "Intensity": 9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 368.55,
        "Intensity": 0.328,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 368.59,
        "Intensity": 0.0392,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 368.6,
        "Intensity": 75,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 368.8,
        "Intensity": 0.625,
        "Nuclide": "Bi-210m (A 3.04E+6 Y)"
    },
    {
        "E(keV)": 370.0,
        "Intensity": 17.411,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 370.1,
        "Intensity": 98,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 370.17,
        "Intensity": 0.759,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 370.3,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 370.9,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 370.94,
        "Intensity": 0.107,
        "Nuclide": "U-237 (B- 6.75 D)"
    },
    {
        "E(keV)": 371.24,
        "Intensity": 22.241,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 371.68,
        "Intensity": 0.48,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 371.75,
        "Intensity": 0.524,
        "Nuclide": "Dy-166 (B- 81.6 H)"
    },
    {
        "E(keV)": 371.918,
        "Intensity": 30.484,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 372.507,
        "Intensity": 2.728,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 373.246,
        "Intensity": 14.047,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 373.5,
        "Intensity": 0.00246,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 373.8,
        "Intensity": 3.267,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 374.3,
        "Intensity": 13.068,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 374.4852,
        "Intensity": 0.711,
        "Nuclide": "Ir-192 (EC 73.827 D)"
    },
    {
        "E(keV)": 374.6,
        "Intensity": 0.00314,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 374.8,
        "Intensity": 35.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 374.99,
        "Intensity": 0.309,
        "Nuclide": "Ba-128 (EC 2.43 D)"
    },
    {
        "E(keV)": 374.991,
        "Intensity": 17.214,
        "Nuclide": "Xe-127 (EC 36.4 D)"
    },
    {
        "E(keV)": 375.054,
        "Intensity": 0.001554,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 375.45,
        "Intensity": 0.679,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 376.6,
        "Intensity": 8.122,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 377.0,
        "Intensity": 0.015,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 377.4,
        "Intensity": 0.122,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 377.523,
        "Intensity": 3.432,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 377.6,
        "Intensity": 6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 378.5029,
        "Intensity": 29.745,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 378.624,
        "Intensity": 2.317,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 378.7,
        "Intensity": 3,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 379.5,
        "Intensity": 14.1,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 379.8,
        "Intensity": 3,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 379.8,
        "Intensity": 14,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 379.94,
        "Intensity": 0.03778,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 380.13,
        "Intensity": 0.01043,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 380.2,
        "Intensity": 14,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 380.452,
        "Intensity": 1.527,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 380.8,
        "Intensity": 2.396,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 380.8,
        "Intensity": 3.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 380.9,
        "Intensity": 1.768,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 381.1,
        "Intensity": 0.00555,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 381.17,
        "Intensity": 1.846,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 381.4,
        "Intensity": 9.966,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 381.43,
        "Intensity": 7.76,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 381.53,
        "Intensity": 10.432,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 381.7,
        "Intensity": 0.003482,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 382.0,
        "Intensity": 0.018,
        "Nuclide": "Fe-59 (B- 44.503 D)"
    },
    {
        "E(keV)": 382.1,
        "Intensity": 0.05573,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 382.2,
        "Intensity": 6.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 382.9,
        "Intensity": 6e-05,
        "Nuclide": "Sn-113 (EC 115.09 D)"
    },
    {
        "E(keV)": 383.1,
        "Intensity": 10,
        "Nuclide": "Cf,248CM-252 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 383.5,
        "Intensity": 0.04663,
        "Nuclide": "Gd-146 (EC 48.27 D)"
    },
    {
        "E(keV)": 383.501,
        "Intensity": 2.349,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 383.6,
        "Intensity": 0.03587,
        "Nuclide": "Pa-230 (B- 17.4 D)"
    },
    {
        "E(keV)": 383.6,
        "Intensity": 4.65,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 383.848,
        "Intensity": 9.235,
        "Nuclide": "Ba-133 (EC 10.52 Y)"
    },
    {
        "E(keV)": 383.851,
        "Intensity": 0.0024,
        "Nuclide": "Xe-133 (B- 5.243 D)"
    },
    {
        "E(keV)": 384.0,
        "Intensity": 0.0055,
        "Nuclide": "Bi-210m (A 3.04E+6 Y)"
    },
    {
        "E(keV)": 384.25,
        "Intensity": 3.133,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 384.8,
        "Intensity": 70,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 385.0,
        "Intensity": 0.05,
        "Nuclide": "Es-254 (A 275.7 D)"
    },
    {
        "E(keV)": 385.0,
        "Intensity": 0.567,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 385.6,
        "Intensity": 0.158,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 386.0,
        "Intensity": 0.0013,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 386.4,
        "Intensity": 0.271,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 387.1,
        "Intensity": 0.0181,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 387.48,
        "Intensity": 1.26,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 387.87,
        "Intensity": 2.133,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 387.884,
        "Intensity": 6.97,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 388.16,
        "Intensity": 66,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 388.531,
        "Intensity": 81.936,
        "Nuclide": "Y-87 (EC 79.8 H)"
    },
    {
        "E(keV)": 388.633,
        "Intensity": 34.073,
        "Nuclide": "I-126 (B- 13.11 D)"
    },
    {
        "E(keV)": 388.7,
        "Intensity": 8.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 388.97,
        "Intensity": 1.41,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 389.18,
        "Intensity": 0.0264,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 389.2,
        "Intensity": 6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 389.37,
        "Intensity": 1.228,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 389.404,
        "Intensity": 2.848,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 390.7,
        "Intensity": 23,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 390.8,
        "Intensity": 35,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 391.383,
        "Intensity": 0.431,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 391.698,
        "Intensity": 64.971,
        "Nuclide": "Sn-113 (EC 115.09 D)"
    },
    {
        "E(keV)": 391.7,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 391.8,
        "Intensity": 0.957,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 392.4,
        "Intensity": 91,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 392.514,
        "Intensity": 1.336,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 392.64,
        "Intensity": 2.053,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 393.14,
        "Intensity": 0.000348,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 393.2,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 393.4,
        "Intensity": 1.3,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 393.4,
        "Intensity": 0.01006,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 393.529,
        "Intensity": 0.22,
        "Nuclide": "Cu-67 (B- 61.83 H)"
    },
    {
        "E(keV)": 393.529,
        "Intensity": 4.671,
        "Nuclide": "Ga-67 (EC 3.2612 D)"
    },
    {
        "E(keV)": 393.7,
        "Intensity": 24,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 393.8,
        "Intensity": 0.01554,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 393.8,
        "Intensity": 16.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 394.5,
        "Intensity": 2.198,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 394.9,
        "Intensity": 4.158,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 396.0,
        "Intensity": 34.821,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 396.329,
        "Intensity": 6.4,
        "Nuclide": "Yb-175 (B- 4.185 D)"
    },
    {
        "E(keV)": 397.0,
        "Intensity": 15,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 397.36,
        "Intensity": 6.383,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 397.54,
        "Intensity": 8.707,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 397.7,
        "Intensity": 1.713,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 398.0,
        "Intensity": 10.929,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 398.09,
        "Intensity": 0.06277,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 398.155,
        "Intensity": 0.87,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 398.62,
        "Intensity": 1.39,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 399.57,
        "Intensity": 0.129,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 399.7,
        "Intensity": 0.122,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 400.1,
        "Intensity": 464,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 400.6572,
        "Intensity": 11.402,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 400.7,
        "Intensity": 26,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 401.1,
        "Intensity": 0.374,
        "Nuclide": "Lu-176 (B- 4.00E10 Y)"
    },
    {
        "E(keV)": 401.3,
        "Intensity": 160,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 401.325,
        "Intensity": 3.412,
        "Nuclide": "Pb-203 (EC 51.873 H)"
    },
    {
        "E(keV)": 402.4,
        "Intensity": 72,
        "Nuclide": "Cm-247 (A 1.56E+7 Y)"
    },
    {
        "E(keV)": 403.5,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 403.5,
        "Intensity": 10,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 404.046,
        "Intensity": 1.311,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 404.2,
        "Intensity": 0.0022,
        "Nuclide": "Ra-224 (A 3.66 D)"
    },
    {
        "E(keV)": 404.814,
        "Intensity": 0.05474,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 405.0,
        "Intensity": 0.084,
        "Nuclide": "Fm-253 (A 3.00 D)"
    },
    {
        "E(keV)": 405.8,
        "Intensity": 5.5,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 406.0,
        "Intensity": 27,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 406.182,
        "Intensity": 13.619,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 407.22,
        "Intensity": 4.448,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 407.22,
        "Intensity": 23.353,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 407.338,
        "Intensity": 42.1,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 407.8,
        "Intensity": 0.02786,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 407.8,
        "Intensity": 144,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 408.4,
        "Intensity": 66,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 408.7,
        "Intensity": 0.186,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 409.44,
        "Intensity": 8.766,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 409.6,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 409.72,
        "Intensity": 21.429,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 410.48,
        "Intensity": 0.14,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 410.8,
        "Intensity": 23,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 410.8,
        "Intensity": 40.59,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 410.944,
        "Intensity": 11.413,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 411.1,
        "Intensity": 1.557e-05,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 411.1163,
        "Intensity": 2.234,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 411.49,
        "Intensity": 22.223,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 411.491,
        "Intensity": 0.01456,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 411.80205,
        "Intensity": 95.58,
        "Nuclide": "Au-198 (B- 2.69517 D)"
    },
    {
        "E(keV)": 412.1,
        "Intensity": 3.827,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 412.8,
        "Intensity": 6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 413.6636,
        "Intensity": 17.372,
        "Nuclide": "Lu-177m (IT 160.4 D)"
    },
    {
        "E(keV)": 413.713,
        "Intensity": 0.001466,
        "Nuclide": "Pu-239 (A 24110 Y)"
    },
    {
        "E(keV)": 414.028,
        "Intensity": 10.452,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 414.057,
        "Intensity": 10.233,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 414.07,
        "Intensity": 18.585,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 414.6,
        "Intensity": 29,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 414.6,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 414.6,
        "Intensity": 0.0003,
        "Nuclide": "Ra-226 (A 1600 Y)"
    },
    {
        "E(keV)": 414.8,
        "Intensity": 83.266,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 415.25,
        "Intensity": 2.243,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 415.3,
        "Intensity": 15,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 415.76,
        "Intensity": 1.745,
        "Nuclide": "Pa-233 (B- 26.967 D)"
    },
    {
        "E(keV)": 416.4688,
        "Intensity": 0.669,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 417.24,
        "Intensity": 0.663,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 417.7,
        "Intensity": 14,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 417.7,
        "Intensity": 22,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 417.8,
        "Intensity": 15.1,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 417.86,
        "Intensity": 0.003792,
        "Nuclide": "Rh-101m (EC 4.34 D)"
    },
    {
        "E(keV)": 418.2,
        "Intensity": 2.537,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 418.37,
        "Intensity": 3.27,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 418.44,
        "Intensity": 0.003658,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 418.5,
        "Intensity": 0.22,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 418.52,
        "Intensity": 10.039,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 418.52,
        "Intensity": 0.07703,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 418.5391,
        "Intensity": 21.255,
        "Nuclide": "Lu-177m (B- 160.4 D)"
    },
    {
        "E(keV)": 418.8,
        "Intensity": 0.01177,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 420.4,
        "Intensity": 3.418,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 420.52,
        "Intensity": 0.06754,
        "Nuclide": "Ir-192 (EC 73.827 D)"
    },
    {
        "E(keV)": 420.7,
        "Intensity": 1.462,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 420.8,
        "Intensity": 0.03098,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 421.6,
        "Intensity": 0.06529,
        "Nuclide": "Gd-146 (EC 48.27 D)"
    },
    {
        "E(keV)": 421.932,
        "Intensity": 2.517,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 422.04,
        "Intensity": 0.003,
        "Nuclide": "Ra-224 (A 3.66 D)"
    },
    {
        "E(keV)": 422.19,
        "Intensity": 0.199,
        "Nuclide": "Rh-101 (EC 3.3 Y)"
    },
    {
        "E(keV)": 422.34,
        "Intensity": 7.955,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 422.4,
        "Intensity": 0.125,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 422.5,
        "Intensity": 74,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 423.0,
        "Intensity": 94,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 423.0,
        "Intensity": 1.9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 423.34,
        "Intensity": 4.535,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 423.63,
        "Intensity": 1.179,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 423.722,
        "Intensity": 3.151,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 424.2,
        "Intensity": 24,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 424.6,
        "Intensity": 0.103,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 425.99,
        "Intensity": 0.58,
        "Nuclide": "Dy-166 (B- 81.6 H)"
    },
    {
        "E(keV)": 426.1,
        "Intensity": 6.631,
        "Nuclide": "Au-196 (B- 6.183 D)"
    },
    {
        "E(keV)": 426.3,
        "Intensity": 36,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 426.36,
        "Intensity": 97.017,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 427.874,
        "Intensity": 29.8,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 428.0,
        "Intensity": 3.12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 428.0,
        "Intensity": 4.56,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 428.5,
        "Intensity": 19,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 428.5,
        "Intensity": 19,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 428.8,
        "Intensity": 4.35,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 428.94,
        "Intensity": 0.00604,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 429.646,
        "Intensity": 13.352,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 430.386,
        "Intensity": 4.51,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 430.634,
        "Intensity": 4.121,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 430.634,
        "Intensity": 0.0015,
        "Nuclide": "Bk-245 (A 4.94 D)"
    },
    {
        "E(keV)": 431.0,
        "Intensity": 3.1,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 431.3,
        "Intensity": 84,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 431.4,
        "Intensity": 5.225e-05,
        "Nuclide": "Sm-145 (EC 340 D)"
    },
    {
        "E(keV)": 431.4,
        "Intensity": 73,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 432.0,
        "Intensity": 0.006679,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 432.493,
        "Intensity": 2.9,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 432.745,
        "Intensity": 2.873,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 432.78,
        "Intensity": 5.326,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 432.999,
        "Intensity": 0.159,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 433.0,
        "Intensity": 1.497,
        "Nuclide": "Hf-175 (EC 70 D)"
    },
    {
        "E(keV)": 433.1,
        "Intensity": 0.00289,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 433.3,
        "Intensity": 12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 433.3,
        "Intensity": 93,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 433.937,
        "Intensity": 90.478,
        "Nuclide": "Ag-108m (EC 418 Y)"
    },
    {
        "E(keV)": 434.71,
        "Intensity": 0.745,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 435.0,
        "Intensity": 50,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 437.575,
        "Intensity": 1.929,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 437.6,
        "Intensity": 2.376,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 438.16,
        "Intensity": 0.634,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 439.401,
        "Intensity": 82.457,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 439.47,
        "Intensity": 1.554,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 439.493,
        "Intensity": 0.001018,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 439.56,
        "Intensity": 91.391,
        "Nuclide": "Tl-202 (EC 12.23 D)"
    },
    {
        "E(keV)": 439.895,
        "Intensity": 1.2,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 440.85,
        "Intensity": 1.508,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 442.8,
        "Intensity": 0.04202,
        "Nuclide": "Rh-105 (B- 35.36 H)"
    },
    {
        "E(keV)": 442.8,
        "Intensity": 1.955,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 443.37,
        "Intensity": 10.844,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 443.555,
        "Intensity": 0.308,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 443.75,
        "Intensity": 5.039,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 443.79,
        "Intensity": 1.503e-05,
        "Nuclide": "Pd-103 (EC 16.991 D)"
    },
    {
        "E(keV)": 443.8,
        "Intensity": 0.345,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 443.965,
        "Intensity": 2.827,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 444.4,
        "Intensity": 13,
        "Nuclide": "Cf,248CM-252 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 444.7,
        "Intensity": 52,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 444.7,
        "Intensity": 52,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 445.03,
        "Intensity": 1.274,
        "Nuclide": "Ra-223 (A 11.435 D)"
    },
    {
        "E(keV)": 445.1,
        "Intensity": 4.342,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 445.68,
        "Intensity": 4.005,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 446.025,
        "Intensity": 2.955,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 446.811,
        "Intensity": 3.723,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 447.0,
        "Intensity": 62,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 447.45,
        "Intensity": 0.05992,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 447.515,
        "Intensity": 23.921,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 447.8,
        "Intensity": 16,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 448.2,
        "Intensity": 0.000695,
        "Nuclide": "Es-253 (A 20.47 D)"
    },
    {
        "E(keV)": 449.0,
        "Intensity": 0.003269,
        "Nuclide": "Nb-92m (EC 10.15 D)"
    },
    {
        "E(keV)": 449.2,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 449.37,
        "Intensity": 0.00019,
        "Nuclide": "Ra-226 (A 1600 Y)"
    },
    {
        "E(keV)": 449.6,
        "Intensity": 0.007353,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 450.93,
        "Intensity": 1.156,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 450.976,
        "Intensity": 28.663,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 451.0,
        "Intensity": 1.224,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 451.521,
        "Intensity": 2.984,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 452.04,
        "Intensity": 0.202,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 452.4,
        "Intensity": 0.0304,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 452.4,
        "Intensity": 2.046,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 453.59,
        "Intensity": 67.6,
        "Nuclide": "Hf-179m (IT 25.05 D)"
    },
    {
        "E(keV)": 453.655,
        "Intensity": 8.615,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 453.88,
        "Intensity": 65.91,
        "Nuclide": "Pm-146 (EC 5.53 Y)"
    },
    {
        "E(keV)": 454.05,
        "Intensity": 16.656,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 454.2,
        "Intensity": 136,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 454.69,
        "Intensity": 0.154,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 454.95,
        "Intensity": 5.744,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 454.95,
        "Intensity": 2.5e-05,
        "Nuclide": "U-234 (A 2.457E+5 Y)"
    },
    {
        "E(keV)": 456.4,
        "Intensity": 1.436,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 456.47,
        "Intensity": 3.682,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 456.7,
        "Intensity": 3.15,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 456.79,
        "Intensity": 0.142,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 456.8,
        "Intensity": 1.98,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 456.8,
        "Intensity": 35,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 457.2,
        "Intensity": 10.2,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 457.6,
        "Intensity": 90.6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 457.6,
        "Intensity": 0.008127,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 457.6,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 459.6,
        "Intensity": 0.001251,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 460.04,
        "Intensity": 0.427,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 460.263,
        "Intensity": 4.16,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 460.49,
        "Intensity": 3.95,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 460.56,
        "Intensity": 0.121,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 460.57,
        "Intensity": 0.417,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 462.6,
        "Intensity": 0.142,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 462.9,
        "Intensity": 2,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 463.1,
        "Intensity": 3.113e-05,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 463.273,
        "Intensity": 1.246,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 463.365,
        "Intensity": 10.564,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 463.38,
        "Intensity": 1.793,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 463.4,
        "Intensity": 5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 463.6,
        "Intensity": 0.756,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 463.6,
        "Intensity": 0.0146,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 463.9,
        "Intensity": 18,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 464.47,
        "Intensity": 1.726,
        "Nuclide": "Cs-132 (B- 6.479 D)"
    },
    {
        "E(keV)": 465.5,
        "Intensity": 10,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 466.5,
        "Intensity": 13,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 467.36,
        "Intensity": 0.28,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 467.5,
        "Intensity": 0.001951,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 467.8,
        "Intensity": 4.4,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 468.0688,
        "Intensity": 47.81,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 468.3,
        "Intensity": 12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 468.58,
        "Intensity": 1.862,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 469.0,
        "Intensity": 1.033,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 469.2,
        "Intensity": 2.52,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 469.85,
        "Intensity": 1.484,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 470.0,
        "Intensity": 3.2,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 470.472,
        "Intensity": 1.405,
        "Nuclide": "Te-121 (EC 16.78 D)"
    },
    {
        "E(keV)": 471.8,
        "Intensity": 0.0264,
        "Nuclide": "Bk-245 (A 4.94 D)"
    },
    {
        "E(keV)": 471.805,
        "Intensity": 72.367,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 472.3,
        "Intensity": 8,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 472.39,
        "Intensity": 4.162,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 472.71,
        "Intensity": 0.03115,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 472.8,
        "Intensity": 31,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 473.0,
        "Intensity": 0.105,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 473.0,
        "Intensity": 25.797,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 473.7,
        "Intensity": 46,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 473.9,
        "Intensity": 24,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 475.0,
        "Intensity": 23.12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 475.0,
        "Intensity": 9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 475.06,
        "Intensity": 101.46,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 475.06,
        "Intensity": 29.529,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 475.1,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 475.365,
        "Intensity": 1.486,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 475.445,
        "Intensity": 1.04,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 475.658,
        "Intensity": 0.01816,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 475.99,
        "Intensity": 0.703,
        "Nuclide": "Hf-181 (B- 42.39 D)"
    },
    {
        "E(keV)": 476.4,
        "Intensity": 1.5e-06,
        "Nuclide": "Re-186 (B- 3.7183 D)"
    },
    {
        "E(keV)": 476.78,
        "Intensity": 41.892,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 477.606,
        "Intensity": 10.52,
        "Nuclide": "Be-7 (EC 53.29 D)"
    },
    {
        "E(keV)": 477.99,
        "Intensity": 15.473,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 478.0,
        "Intensity": 1.425e-06,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 478.0,
        "Intensity": 2.218,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 478.3,
        "Intensity": 1.854,
        "Nuclide": "Pt-188 (EC 10.2 D)"
    },
    {
        "E(keV)": 478.3,
        "Intensity": 8.316,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 480.44,
        "Intensity": 36.964,
        "Nuclide": "Ni-56 (EC 6.075 D)"
    },
    {
        "E(keV)": 481.8,
        "Intensity": 1.235,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 481.8,
        "Intensity": 20.79,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 482.0,
        "Intensity": 71,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 482.18,
        "Intensity": 80.5,
        "Nuclide": "Hf-181 (B- 42.39 D)"
    },
    {
        "E(keV)": 482.6,
        "Intensity": 97,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 483.7,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 483.76,
        "Intensity": 0.001968,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 484.471,
        "Intensity": 0.29,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 484.5751,
        "Intensity": 3.12,
        "Nuclide": "Ir-192 (EC 73.827 D)"
    },
    {
        "E(keV)": 484.805,
        "Intensity": 89.556,
        "Nuclide": "Y-87 (EC 79.8 H)"
    },
    {
        "E(keV)": 484.9,
        "Intensity": 3.06,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 485.9,
        "Intensity": 14,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 486.4,
        "Intensity": 0.331,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 486.5,
        "Intensity": 46,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 486.522,
        "Intensity": 2.088,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 487.0,
        "Intensity": 4.896,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 487.0,
        "Intensity": 13.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 487.021,
        "Intensity": 45.506,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 487.8,
        "Intensity": 15,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 487.9,
        "Intensity": 68,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 487.9,
        "Intensity": 20.1,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 488.2,
        "Intensity": 0.01393,
        "Nuclide": "Bk-245 (EC 4.94 D)"
    },
    {
        "E(keV)": 489.06,
        "Intensity": 0.429,
        "Nuclide": "Ir-192 (EC 73.827 D)"
    },
    {
        "E(keV)": 489.23,
        "Intensity": 6.248,
        "Nuclide": "Ca-47 (B- 4.536 D)"
    },
    {
        "E(keV)": 489.24,
        "Intensity": 0.153,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 490.368,
        "Intensity": 2.161,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 490.4,
        "Intensity": 72,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 490.422,
        "Intensity": 0.414,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 490.6,
        "Intensity": 6.555,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 491.243,
        "Intensity": 2.848,
        "Nuclide": "I-126 (B- 13.11 D)"
    },
    {
        "E(keV)": 491.5,
        "Intensity": 0.03098,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 492.351,
        "Intensity": 8.03,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 492.351,
        "Intensity": 0.0096,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 492.55,
        "Intensity": 0.003281,
        "Nuclide": "Sm-145 (EC 340 D)"
    },
    {
        "E(keV)": 492.9,
        "Intensity": 5.935,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 493.1,
        "Intensity": 9.198,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 493.5,
        "Intensity": 0.125,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 494.169,
        "Intensity": 0.06897,
        "Nuclide": "Ga-67 (EC 3.2612 D)"
    },
    {
        "E(keV)": 495.013,
        "Intensity": 71.328,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 496.326,
        "Intensity": 46.823,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 496.383,
        "Intensity": 1.759,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 497.0,
        "Intensity": 1.04,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 497.06,
        "Intensity": 15.579,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 497.08,
        "Intensity": 0.003963,
        "Nuclide": "Pd-103 (EC 16.991 D)"
    },
    {
        "E(keV)": 497.084,
        "Intensity": 91,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 497.81,
        "Intensity": 0.04451,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 499.1,
        "Intensity": 8.4,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 499.876,
        "Intensity": 2.59,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 501.26,
        "Intensity": 6.718,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 502.06,
        "Intensity": 0.148,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 502.8,
        "Intensity": 0.773,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 502.8,
        "Intensity": 41.9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 503.004,
        "Intensity": 0.36,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 503.1,
        "Intensity": 17,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 503.474,
        "Intensity": 0.149,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 503.5,
        "Intensity": 9.5e-07,
        "Nuclide": "U-234 (A 2.457E+5 Y)"
    },
    {
        "E(keV)": 503.6,
        "Intensity": 1.45e-05,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 503.9,
        "Intensity": 6.318e-05,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 504.4,
        "Intensity": 0.247,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 504.45,
        "Intensity": 0.603,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 505.521,
        "Intensity": 4.926,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 505.79,
        "Intensity": 0.728,
        "Nuclide": "Cs-132 (EC 6.479 D)"
    },
    {
        "E(keV)": 506.093,
        "Intensity": 0.555,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 506.1,
        "Intensity": 19,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 506.2,
        "Intensity": 13.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 506.9,
        "Intensity": 7.84e-06,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 507.188,
        "Intensity": 0.967,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 507.36,
        "Intensity": 0.00026,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 507.591,
        "Intensity": 17.666,
        "Nuclide": "Te-121 (EC 16.78 D)"
    },
    {
        "E(keV)": 507.9,
        "Intensity": 0.07571,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 508.1,
        "Intensity": 0.07041,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 508.2,
        "Intensity": 3.275,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 508.2,
        "Intensity": 1.5e-05,
        "Nuclide": "U-234 (A 2.457E+5 Y)"
    },
    {
        "E(keV)": 508.3,
        "Intensity": 6.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 508.7,
        "Intensity": 11,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 509.3,
        "Intensity": 45,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 509.3,
        "Intensity": 37,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 509.4,
        "Intensity": 0.001336,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 510.0,
        "Intensity": 0.076,
        "Nuclide": "Rn-222 (A 3.8235 D)"
    },
    {
        "E(keV)": 510.9,
        "Intensity": 19,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 510.9,
        "Intensity": 19,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 511.0,
        "Intensity": 24.4,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 511.36,
        "Intensity": 24.054,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 511.8,
        "Intensity": 36,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 511.85,
        "Intensity": 89.016,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 512.6,
        "Intensity": 0.809,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 513.997,
        "Intensity": 0.434,
        "Nuclide": "Kr-85 (B- 10.756 Y)"
    },
    {
        "E(keV)": 514.0067,
        "Intensity": 99.553,
        "Nuclide": "Sr-85 (EC 64.84 D)"
    },
    {
        "E(keV)": 514.6,
        "Intensity": 0.01138,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 514.8,
        "Intensity": 18.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 515.0,
        "Intensity": 8,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 515.0,
        "Intensity": 8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 515.25,
        "Intensity": 4.5e-06,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 515.6,
        "Intensity": 0.00017,
        "Nuclide": "Pu-236 (A 2.851 Y)"
    },
    {
        "E(keV)": 515.607,
        "Intensity": 5.518,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 515.8,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 516.18,
        "Intensity": 41.463,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 516.545,
        "Intensity": 2.858,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 518.0,
        "Intensity": 5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 518.5,
        "Intensity": 1.814,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 518.55,
        "Intensity": 33.14,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 519.2,
        "Intensity": 6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 519.4,
        "Intensity": 36,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 520.13,
        "Intensity": 0.585,
        "Nuclide": "Tl-202 (EC 12.23 D)"
    },
    {
        "E(keV)": 520.389,
        "Intensity": 46.236,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 520.654,
        "Intensity": 0.558,
        "Nuclide": "As-77 (B- 38.83 H)"
    },
    {
        "E(keV)": 520.69,
        "Intensity": 22.264,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 520.8,
        "Intensity": 0.00033,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 521.1,
        "Intensity": 7.325e-06,
        "Nuclide": "Pu-237 (A 45.2 D)"
    },
    {
        "E(keV)": 521.1,
        "Intensity": 12,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 521.4,
        "Intensity": 0.388,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 522.4,
        "Intensity": 0.0009352,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 522.47,
        "Intensity": 15.726,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 522.7,
        "Intensity": 41,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 523.2,
        "Intensity": 0.213,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 523.6,
        "Intensity": 9.4,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 524.2,
        "Intensity": 31,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 524.2,
        "Intensity": 31,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 524.3,
        "Intensity": 0.002071,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 525.1,
        "Intensity": 5.6,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 525.35,
        "Intensity": 0.367,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 525.75,
        "Intensity": 0.486,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 526.642,
        "Intensity": 0.615,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 527.0,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 527.901,
        "Intensity": 27.45,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 528.1,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 528.24,
        "Intensity": 33.143,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 528.26,
        "Intensity": 4.143,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 528.3,
        "Intensity": 4.2,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 528.587,
        "Intensity": 0.505,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 528.76,
        "Intensity": 1.651,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 528.788,
        "Intensity": 0.05701,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 529.1,
        "Intensity": 0.0532,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 529.5,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 529.591,
        "Intensity": 30.331,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 529.8,
        "Intensity": 2.625,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 529.801,
        "Intensity": 9.692,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 530.1,
        "Intensity": 60,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 530.6,
        "Intensity": 0.09088,
        "Nuclide": "Ca-47 (B- 4.536 D)"
    },
    {
        "E(keV)": 530.7,
        "Intensity": 1.2,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 531.016,
        "Intensity": 13.085,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 531.06,
        "Intensity": 0.002652,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 531.4,
        "Intensity": 0.06258,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 531.5,
        "Intensity": 1.6,
        "Nuclide": "Tm-167 (EC 9.25 D)"
    },
    {
        "E(keV)": 532.66,
        "Intensity": 0.207,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 533.2,
        "Intensity": 0.03189,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 534.29,
        "Intensity": 66.588,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 534.295,
        "Intensity": 3.257,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 534.6,
        "Intensity": 6,
        "Nuclide": "Cf,248CM-252 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 535.036,
        "Intensity": 9.41,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 535.143,
        "Intensity": 0.293,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 535.4,
        "Intensity": 0.109,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 535.5,
        "Intensity": 0.255,
        "Nuclide": "Bi-210m (A 3.04E+6 Y)"
    },
    {
        "E(keV)": 535.7,
        "Intensity": 9,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 535.78,
        "Intensity": 0.407,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 535.897,
        "Intensity": 0.04775,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 535.9,
        "Intensity": 0.01147,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 536.674,
        "Intensity": 3.301,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 537.261,
        "Intensity": 24.39,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 537.45,
        "Intensity": 30.996,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 538.09,
        "Intensity": 1.47e-07,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 538.3,
        "Intensity": 8.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 538.87,
        "Intensity": 14.991,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 539.0,
        "Intensity": 3.5e-05,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 539.1,
        "Intensity": 0.0002838,
        "Nuclide": "Po-208 (EC 2.898 Y)"
    },
    {
        "E(keV)": 539.1,
        "Intensity": 0.02175,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 539.22,
        "Intensity": 0.326,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 540.1,
        "Intensity": 8,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 540.4,
        "Intensity": 0.04841,
        "Nuclide": "Ac-226 (B- 29.37 H)"
    },
    {
        "E(keV)": 540.7,
        "Intensity": 22,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 542.0,
        "Intensity": 1.584,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 542.0,
        "Intensity": 4,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 542.57,
        "Intensity": 4.418,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 543.0,
        "Intensity": 3.4,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 543.3,
        "Intensity": 2.944,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 544.458,
        "Intensity": 0.882,
        "Nuclide": "Es-254m (B- 39.3 H)"
    },
    {
        "E(keV)": 544.9,
        "Intensity": 47,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 545.117,
        "Intensity": 4.019,
        "Nuclide": "Rh-101m (EC 4.34 D)"
    },
    {
        "E(keV)": 546.8,
        "Intensity": 2.648,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 547.0,
        "Intensity": 11,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 547.0,
        "Intensity": 1.01e-06,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 547.8,
        "Intensity": 6.93,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 548.945,
        "Intensity": 3.384,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 549.84,
        "Intensity": 2.994,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 550.249,
        "Intensity": 0.03621,
        "Nuclide": "Tb-161 (B- 6.88 D)"
    },
    {
        "E(keV)": 550.27,
        "Intensity": 94.476,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 550.27,
        "Intensity": 22,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 550.284,
        "Intensity": 100.136,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 551.08,
        "Intensity": 0.003122,
        "Nuclide": "Ba-140 (B- 12.752 D)"
    },
    {
        "E(keV)": 551.1,
        "Intensity": 39,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 551.8,
        "Intensity": 5.454e-07,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 552.3,
        "Intensity": 12,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 552.588,
        "Intensity": 16.506,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 553.0,
        "Intensity": 0.109,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 553.231,
        "Intensity": 13.157,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 553.26,
        "Intensity": 5.116,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 553.35,
        "Intensity": 0.526,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 554.348,
        "Intensity": 70.758,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 554.5,
        "Intensity": 7.889e-05,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 554.64,
        "Intensity": 1.557,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 555.2,
        "Intensity": 1.693,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 555.8,
        "Intensity": 59,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 556.6,
        "Intensity": 96.2,
        "Nuclide": "Rh-102 (B- 207 D)"
    },
    {
        "E(keV)": 556.65,
        "Intensity": 0.121,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 556.9,
        "Intensity": 14,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 557.04,
        "Intensity": 0.868,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 557.36,
        "Intensity": 1.304,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 557.4,
        "Intensity": 8,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 557.497,
        "Intensity": 0.525,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 557.5,
        "Intensity": 20,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 557.95,
        "Intensity": 29.359,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 558.37,
        "Intensity": 0.01519,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 558.372,
        "Intensity": 0.05173,
        "Nuclide": "Eu-149 (EC 93.1 D)"
    },
    {
        "E(keV)": 558.43,
        "Intensity": 3.238,
        "Nuclide": "In-114m (EC 49.51 D)"
    },
    {
        "E(keV)": 559.07,
        "Intensity": 6.542,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 559.1,
        "Intensity": 45,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 559.26,
        "Intensity": 0.486,
        "Nuclide": "Os-193 (B- 30.11 H)"
    },
    {
        "E(keV)": 560.27,
        "Intensity": 6.949,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 560.34,
        "Intensity": 0.03251,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 560.9,
        "Intensity": 1.224,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 561.0,
        "Intensity": 0.004458,
        "Nuclide": "Nb-92m (EC 10.15 D)"
    },
    {
        "E(keV)": 561.02,
        "Intensity": 0.00015,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 561.1,
        "Intensity": 134,
        "Nuclide": "Nb-92 (EC 3.47E7 Y)"
    },
    {
        "E(keV)": 561.1,
        "Intensity": 2,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 561.11,
        "Intensity": 0.114,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 561.88,
        "Intensity": 0.01298,
        "Nuclide": "Nb-95 (B- 34.975 D)"
    },
    {
        "E(keV)": 561.9,
        "Intensity": 14,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 562.17,
        "Intensity": 0.008785,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 562.4,
        "Intensity": 35,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 562.4,
        "Intensity": 35,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 563.197,
        "Intensity": 3.678,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 563.2,
        "Intensity": 0.0001,
        "Nuclide": "Pu-236 (A 2.851 Y)"
    },
    {
        "E(keV)": 563.23,
        "Intensity": 1.202,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 563.246,
        "Intensity": 8.35,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 563.41,
        "Intensity": 0.495,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 563.48,
        "Intensity": 0.00937,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 563.5,
        "Intensity": 5,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 563.99,
        "Intensity": 0.49,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 564.0,
        "Intensity": 1.465,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 564.183,
        "Intensity": 2.331,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 564.2,
        "Intensity": 6.732,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 564.24,
        "Intensity": 70.675,
        "Nuclide": "Sb-122 (B- 2.7238 D)"
    },
    {
        "E(keV)": 565.2,
        "Intensity": 11.3,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 566.2,
        "Intensity": 47,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 566.4,
        "Intensity": 40,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 566.6,
        "Intensity": 34.428,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 567.16,
        "Intensity": 0.234,
        "Nuclide": "Cs-132 (B- 6.479 D)"
    },
    {
        "E(keV)": 567.2,
        "Intensity": 25,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 567.6,
        "Intensity": 0.279,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 568.36,
        "Intensity": 0.0186,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 568.88,
        "Intensity": 0.913,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 569.1,
        "Intensity": 2.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 569.29,
        "Intensity": 0.873,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 569.3,
        "Intensity": 27.802,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 569.331,
        "Intensity": 15.38,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 569.4,
        "Intensity": 14,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 569.4,
        "Intensity": 14,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 569.702,
        "Intensity": 97.75,
        "Nuclide": "Bi-207 (EC 31.55 Y)"
    },
    {
        "E(keV)": 570.09,
        "Intensity": 0.0158,
        "Nuclide": "Co-57 (EC 271.74 D)"
    },
    {
        "E(keV)": 570.5,
        "Intensity": 0.42,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 570.5,
        "Intensity": 3.333e-06,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 570.6,
        "Intensity": 4.398,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 570.7,
        "Intensity": 0.0007838,
        "Nuclide": "Po-208 (EC 2.898 Y)"
    },
    {
        "E(keV)": 570.8,
        "Intensity": 0.006853,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 570.99,
        "Intensity": 5.547,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 571.1,
        "Intensity": 0.993,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 571.5,
        "Intensity": 0.14,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 571.962,
        "Intensity": 9.721,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 572.2,
        "Intensity": 0.03537,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 572.255,
        "Intensity": 0.188,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 573.139,
        "Intensity": 80.3,
        "Nuclide": "Te-121 (EC 16.78 D)"
    },
    {
        "E(keV)": 573.5,
        "Intensity": 12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 573.6,
        "Intensity": 7.2,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 573.8,
        "Intensity": 6.673,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 574.0,
        "Intensity": 0.21,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 574.11,
        "Intensity": 10.192,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 574.215,
        "Intensity": 87.889,
        "Nuclide": "Hf-178m (IT 31 Y)"
    },
    {
        "E(keV)": 574.5,
        "Intensity": 0.06992,
        "Nuclide": "Ac-226 (B- 29.37 H)"
    },
    {
        "E(keV)": 574.64,
        "Intensity": 1.18,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 574.8,
        "Intensity": 0.0003,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 575.5,
        "Intensity": 46,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 575.52,
        "Intensity": 0.208,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 576.0,
        "Intensity": 0.06529,
        "Nuclide": "Gd-146 (EC 48.27 D)"
    },
    {
        "E(keV)": 576.1,
        "Intensity": 1.19,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 576.6,
        "Intensity": 1.7,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 578.5,
        "Intensity": 11.7,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 578.6,
        "Intensity": 3,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 578.8,
        "Intensity": 6,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 578.91,
        "Intensity": 2.938,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 579.28,
        "Intensity": 13.701,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 579.78,
        "Intensity": 1.057,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 579.8,
        "Intensity": 5.521,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 580.3,
        "Intensity": 7,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 580.3,
        "Intensity": 7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 581.398,
        "Intensity": 6.002,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 581.7,
        "Intensity": 1.2e-05,
        "Nuclide": "U-234 (A 2.457E+5 Y)"
    },
    {
        "E(keV)": 582.01,
        "Intensity": 0.889,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 582.07,
        "Intensity": 0.05475,
        "Nuclide": "Nb-95m (B- 86.6 H)"
    },
    {
        "E(keV)": 582.082,
        "Intensity": 29.589,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 582.3,
        "Intensity": 61,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 582.4,
        "Intensity": 55.266,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 582.4,
        "Intensity": 0.189,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 583.0,
        "Intensity": 21.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 584.274,
        "Intensity": 53.986,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 584.318,
        "Intensity": 2.842,
        "Nuclide": "Es-254m (B- 39.3 H)"
    },
    {
        "E(keV)": 584.4,
        "Intensity": 35,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 584.5,
        "Intensity": 6.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 584.6,
        "Intensity": 10,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 585.041,
        "Intensity": 1.194,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 585.2,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 585.48,
        "Intensity": 1.559,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 585.7,
        "Intensity": 1.496,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 586.2648,
        "Intensity": 0.459,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 587.1,
        "Intensity": 0.226,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 587.2,
        "Intensity": 0.267,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 588.549,
        "Intensity": 0.601,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 588.581,
        "Intensity": 4.517,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 589.3,
        "Intensity": 6.5,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 589.35,
        "Intensity": 0.04576,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 589.8,
        "Intensity": 0.428,
        "Nuclide": "Pm-146 (EC 5.53 Y)"
    },
    {
        "E(keV)": 589.912,
        "Intensity": 1.84,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 590.0,
        "Intensity": 0.0836,
        "Nuclide": "Es-252 (A 471.7 D)"
    },
    {
        "E(keV)": 590.1,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 590.88,
        "Intensity": 0.06913,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 591.3,
        "Intensity": 0.109,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 591.762,
        "Intensity": 4.962,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 592.074,
        "Intensity": 1.366,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 592.83,
        "Intensity": 0.353,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 593.0,
        "Intensity": 7.47,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 593.3,
        "Intensity": 0.002275,
        "Nuclide": "Te-127m (B- 109 D)"
    },
    {
        "E(keV)": 593.49,
        "Intensity": 0.0421,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 593.5,
        "Intensity": 0.63,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 593.6,
        "Intensity": 2.268,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 594.8,
        "Intensity": 0.265,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 595.375,
        "Intensity": 0.0017,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 595.83,
        "Intensity": 33.297,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 596.7,
        "Intensity": 0.01162,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 597.2,
        "Intensity": 4.9e-05,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 598.4,
        "Intensity": 16,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 598.8,
        "Intensity": 1.008,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 599.2,
        "Intensity": 9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 599.41,
        "Intensity": 0.0039,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 599.61,
        "Intensity": 0.28,
        "Nuclide": "Re-189 (B- 24.3 H)"
    },
    {
        "E(keV)": 599.74,
        "Intensity": 12.487,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 600.16,
        "Intensity": 0.275,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 600.5,
        "Intensity": 62,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 600.597,
        "Intensity": 17.767,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 600.66,
        "Intensity": 0.00049,
        "Nuclide": "Ra-226 (A 1600 Y)"
    },
    {
        "E(keV)": 600.92,
        "Intensity": 0.0381,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 601.45,
        "Intensity": 5.872,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 601.9,
        "Intensity": 5.25,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 602.72,
        "Intensity": 48.387,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 602.7275,
        "Intensity": 98.26,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 602.9,
        "Intensity": 0.0006081,
        "Nuclide": "Po-208 (EC 2.898 Y)"
    },
    {
        "E(keV)": 603.5,
        "Intensity": 4.453,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 603.8,
        "Intensity": 1.632,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 604.0,
        "Intensity": 11.1,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 604.4,
        "Intensity": 0.02159,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 604.41105,
        "Intensity": 8.2,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 604.721,
        "Intensity": 97.62,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 605.04,
        "Intensity": 0.00011,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 605.13,
        "Intensity": 0.081,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 605.14,
        "Intensity": 38.922,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 605.4,
        "Intensity": 10.8,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 605.8,
        "Intensity": 7.35e-06,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 605.91,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 606.09,
        "Intensity": 7.57,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 606.2,
        "Intensity": 0.958,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 606.37,
        "Intensity": 1.211,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 606.7,
        "Intensity": 0.07361,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 606.713,
        "Intensity": 5.015,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 607.0,
        "Intensity": 18,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 607.1,
        "Intensity": 16.308,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 608.43,
        "Intensity": 0.31,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 609.5,
        "Intensity": 0.0146,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 609.5,
        "Intensity": 0.0146,
        "Nuclide": "Sm-153 (B- 46.50 H)"
    },
    {
        "E(keV)": 609.8,
        "Intensity": 6.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 610.062,
        "Intensity": 44.205,
        "Nuclide": "Er-172 (B- 49.3 H)"
    },
    {
        "E(keV)": 610.33,
        "Intensity": 5.76,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 610.4,
        "Intensity": 12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 611.26,
        "Intensity": 5.459,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 611.26,
        "Intensity": 1.021,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 611.293,
        "Intensity": 20.831,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 612.02,
        "Intensity": 0.107,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 612.4621,
        "Intensity": 5.34,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 613.92,
        "Intensity": 0.01488,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 614.276,
        "Intensity": 89.845,
        "Nuclide": "Ag-108m (EC 418 Y)"
    },
    {
        "E(keV)": 614.8,
        "Intensity": 2.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 615.0,
        "Intensity": 0.01131,
        "Nuclide": "Sb-122 (B- 2.7238 D)"
    },
    {
        "E(keV)": 615.17,
        "Intensity": 0.233,
        "Nuclide": "Hf-181 (B- 42.39 D)"
    },
    {
        "E(keV)": 615.365,
        "Intensity": 0.376,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 616.17,
        "Intensity": 21.898,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 616.49,
        "Intensity": 1.268,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 617.0,
        "Intensity": 4e-05,
        "Nuclide": "U-230 (A 20.8 D)"
    },
    {
        "E(keV)": 617.22,
        "Intensity": 8e-06,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 617.36,
        "Intensity": 0.065,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 617.4,
        "Intensity": 0.04303,
        "Nuclide": "Ac-226 (B- 29.37 H)"
    },
    {
        "E(keV)": 617.8,
        "Intensity": 0.00441,
        "Nuclide": "Se-75 (EC 119.79 D)"
    },
    {
        "E(keV)": 617.85,
        "Intensity": 1.196,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 618.01,
        "Intensity": 98.378,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 618.13,
        "Intensity": 3.646,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 618.4,
        "Intensity": 0.01421,
        "Nuclide": "Xe-127 (EC 36.4 D)"
    },
    {
        "E(keV)": 618.66,
        "Intensity": 0.02504,
        "Nuclide": "Hf-181 (B- 42.39 D)"
    },
    {
        "E(keV)": 618.9,
        "Intensity": 10,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 619.0,
        "Intensity": 3.661,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 619.106,
        "Intensity": 43.441,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 619.3,
        "Intensity": 0.0005344,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 620.0,
        "Intensity": 7.979e-07,
        "Nuclide": "Th-230 (A 7.538E+4 Y)"
    },
    {
        "E(keV)": 620.0,
        "Intensity": 0.093,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 620.111,
        "Intensity": 1.437,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 620.3,
        "Intensity": 0.01096,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 620.3,
        "Intensity": 63.3,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 620.36,
        "Intensity": 2.787,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 620.48,
        "Intensity": 5.857,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 621.771,
        "Intensity": 0.02584,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 622.0,
        "Intensity": 0.006012,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 622.05,
        "Intensity": 1.712,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 624.06,
        "Intensity": 1.543,
        "Nuclide": "Pt-191 (EC 2.802 D)"
    },
    {
        "E(keV)": 624.4,
        "Intensity": 8.2e-07,
        "Nuclide": "U-234 (A 2.457E+5 Y)"
    },
    {
        "E(keV)": 624.8,
        "Intensity": 10,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 625.0,
        "Intensity": 0.416,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 625.18,
        "Intensity": 4.748,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 625.5,
        "Intensity": 1.877,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 625.6,
        "Intensity": 5.166,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 627.041,
        "Intensity": 0.835,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 628.05,
        "Intensity": 8.864,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 628.05,
        "Intensity": 2.889,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 628.21,
        "Intensity": 0.01446,
        "Nuclide": "Lu-174m (EC 142 D)"
    },
    {
        "E(keV)": 628.6,
        "Intensity": 8.532e-05,
        "Nuclide": "Te-127m (B- 109 D)"
    },
    {
        "E(keV)": 628.63,
        "Intensity": 0.997,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 629.92,
        "Intensity": 0.958,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 629.97,
        "Intensity": 88.627,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 629.987,
        "Intensity": 73.092,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 630.1,
        "Intensity": 15,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 630.19,
        "Intensity": 0.942,
        "Nuclide": "Cs-132 (EC 6.479 D)"
    },
    {
        "E(keV)": 630.33,
        "Intensity": 0.0293,
        "Nuclide": "Re-186 (B- 3.7183 D)"
    },
    {
        "E(keV)": 631.09,
        "Intensity": 0.000341,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 631.1,
        "Intensity": 10.88,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 631.29,
        "Intensity": 59.808,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 631.29,
        "Intensity": 0.06419,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 631.3,
        "Intensity": 56.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 631.705,
        "Intensity": 9.242,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 632.25,
        "Intensity": 4.549,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 632.5,
        "Intensity": 0.0096,
        "Nuclide": "Ba-133m (EC 38.9 H)"
    },
    {
        "E(keV)": 632.9,
        "Intensity": 0.0291,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 633.02,
        "Intensity": 18.877,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 633.083,
        "Intensity": 34.27,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 633.2,
        "Intensity": 3,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 633.25,
        "Intensity": 2.153,
        "Nuclide": "Pm-146 (B- 5.53 Y)"
    },
    {
        "E(keV)": 634.137,
        "Intensity": 43.025,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 634.78,
        "Intensity": 15.351,
        "Nuclide": "As-74 (B- 17.77 D)"
    },
    {
        "E(keV)": 634.91,
        "Intensity": 5.261,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 635.0,
        "Intensity": 0.01,
        "Nuclide": "Bi-210m (A 3.04E+6 Y)"
    },
    {
        "E(keV)": 635.0,
        "Intensity": 0.0357,
        "Nuclide": "As-74 (B- 17.77 D)"
    },
    {
        "E(keV)": 635.95,
        "Intensity": 11.294,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 636.11,
        "Intensity": 1.469,
        "Nuclide": "Lu-173 (EC 1.37 Y)"
    },
    {
        "E(keV)": 636.2,
        "Intensity": 1.417,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 636.5,
        "Intensity": 0.0093,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 636.5,
        "Intensity": 7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 636.81,
        "Intensity": 0.148,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 636.88,
        "Intensity": 1.558,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 636.989,
        "Intensity": 7.173,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 638.03,
        "Intensity": 0.00097,
        "Nuclide": "Sn-113 (EC 115.09 D)"
    },
    {
        "E(keV)": 639.72,
        "Intensity": 0.008385,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 640.1,
        "Intensity": 1.36,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 640.1,
        "Intensity": 12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 640.1,
        "Intensity": 0.416,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 640.1,
        "Intensity": 12,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 641.6,
        "Intensity": 12,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 641.915,
        "Intensity": 1.932,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 642.35,
        "Intensity": 1.3e-05,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 642.719,
        "Intensity": 0.217,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 644.55,
        "Intensity": 11.444,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 645.0,
        "Intensity": 0.00024,
        "Nuclide": "Pu-236 (A 2.851 Y)"
    },
    {
        "E(keV)": 645.18,
        "Intensity": 2.146,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 645.23,
        "Intensity": 0.0616,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 645.315,
        "Intensity": 1.549,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 645.5,
        "Intensity": 0.0054,
        "Nuclide": "Ra-224 (A 3.66 D)"
    },
    {
        "E(keV)": 645.82,
        "Intensity": 0.76,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 645.8537,
        "Intensity": 7.456,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 646.116,
        "Intensity": 80.823,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 646.29,
        "Intensity": 6.279,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 646.8,
        "Intensity": 38.3,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 646.83,
        "Intensity": 4e-06,
        "Nuclide": "Sn-113 (EC 115.09 D)"
    },
    {
        "E(keV)": 647.47,
        "Intensity": 0.282,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 648.8,
        "Intensity": 28.42,
        "Nuclide": "Es-254m (B- 39.3 H)"
    },
    {
        "E(keV)": 648.97,
        "Intensity": 0.08785,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 649.5,
        "Intensity": 15.4,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 649.7,
        "Intensity": 3.85,
        "Nuclide": "Bi-210m (A 3.04E+6 Y)"
    },
    {
        "E(keV)": 650.72,
        "Intensity": 2.627,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 651.0,
        "Intensity": 0.0002844,
        "Nuclide": "Te-127m (B- 109 D)"
    },
    {
        "E(keV)": 651.7,
        "Intensity": 14.4,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 651.8,
        "Intensity": 0.006916,
        "Nuclide": "Ru-103 (B- 39.26 D)"
    },
    {
        "E(keV)": 652.41,
        "Intensity": 100,
        "Nuclide": "Tc-98 (B- 4.2E+6 Y)"
    },
    {
        "E(keV)": 653.2,
        "Intensity": 0.151,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 653.512,
        "Intensity": 14.878,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 654.8,
        "Intensity": 7,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 654.9,
        "Intensity": 2.2,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 655.3,
        "Intensity": 3.1,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 656.3,
        "Intensity": 2.191,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 657.05,
        "Intensity": 6.165,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 657.7622,
        "Intensity": 94.004,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 658.9,
        "Intensity": 0.01232,
        "Nuclide": "Te-127m (B- 109 D)"
    },
    {
        "E(keV)": 659.1,
        "Intensity": 19,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 659.5,
        "Intensity": 0.003643,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 661.35,
        "Intensity": 2.263,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 661.657,
        "Intensity": 85.1,
        "Nuclide": "Cs-137 (B- 30.04 Y)"
    },
    {
        "E(keV)": 662.24,
        "Intensity": 0.001159,
        "Nuclide": "Am-243 (A 7370 Y)"
    },
    {
        "E(keV)": 662.3,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 664.571,
        "Intensity": 5.692,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 664.65,
        "Intensity": 3.201,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 665.05,
        "Intensity": 4.42,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 665.34,
        "Intensity": 0.365,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 665.424,
        "Intensity": 6.91,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 666.2,
        "Intensity": 0.0816,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 666.289,
        "Intensity": 0.925,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 666.3,
        "Intensity": 99.6,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 666.331,
        "Intensity": 32.778,
        "Nuclide": "I-126 (EC 13.11 D)"
    },
    {
        "E(keV)": 667.404,
        "Intensity": 11.019,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 667.5,
        "Intensity": 0.736,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 667.718,
        "Intensity": 97.113,
        "Nuclide": "Cs-132 (EC 6.479 D)"
    },
    {
        "E(keV)": 670.2,
        "Intensity": 0.583,
        "Nuclide": "Cm-241 (EC 32.8 D)"
    },
    {
        "E(keV)": 670.21,
        "Intensity": 0.008556,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 670.502,
        "Intensity": 5.481,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 671.441,
        "Intensity": 1.803,
        "Nuclide": "Sb-125 (B- 2.75856 Y)"
    },
    {
        "E(keV)": 671.7,
        "Intensity": 2.2,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 671.84,
        "Intensity": 0.02549,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 672.7,
        "Intensity": 24,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 673.21,
        "Intensity": 1.084,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 673.44,
        "Intensity": 0.02769,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 673.5,
        "Intensity": 0.002689,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 674.0,
        "Intensity": 0.0194,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 675.0,
        "Intensity": 3.685,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 675.8836,
        "Intensity": 0.804,
        "Nuclide": "Au-198 (B- 2.69517 D)"
    },
    {
        "E(keV)": 677.516,
        "Intensity": 9.76,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 677.6,
        "Intensity": 1e-06,
        "Nuclide": "U-234 (A 2.457E+5 Y)"
    },
    {
        "E(keV)": 677.6227,
        "Intensity": 10.284,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 677.71,
        "Intensity": 1.473,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 678.623,
        "Intensity": 0.471,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 679.1,
        "Intensity": 9.06,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 680.514,
        "Intensity": 0.768,
        "Nuclide": "Pb-203 (EC 51.873 H)"
    },
    {
        "E(keV)": 680.52,
        "Intensity": 0.01953,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 680.66,
        "Intensity": 0.372,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 680.68,
        "Intensity": 0.215,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 681.18,
        "Intensity": 0.03237,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 681.8,
        "Intensity": 26,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 683.4,
        "Intensity": 6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 685.7,
        "Intensity": 36.8,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 685.9,
        "Intensity": 0.812,
        "Nuclide": "Nd-147 (B- 10.98 D)"
    },
    {
        "E(keV)": 686.0,
        "Intensity": 0.006,
        "Nuclide": "Bi-210m (A 3.04E+6 Y)"
    },
    {
        "E(keV)": 687.015,
        "Intensity": 6.392,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 687.57,
        "Intensity": 3.5e-06,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 687.74,
        "Intensity": 0.002136,
        "Nuclide": "Cs-132 (EC 6.479 D)"
    },
    {
        "E(keV)": 687.8,
        "Intensity": 59,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 688.0,
        "Intensity": 29,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 688.67,
        "Intensity": 0.858,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 688.681,
        "Intensity": 12.25,
        "Nuclide": "Es-254m (B- 39.3 H)"
    },
    {
        "E(keV)": 688.76,
        "Intensity": 0.006072,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 689.286,
        "Intensity": 2.361,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 689.5,
        "Intensity": 10,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 690.23,
        "Intensity": 0.00061,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 690.8,
        "Intensity": 5,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 691.2,
        "Intensity": 12,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 691.4,
        "Intensity": 0.605,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 691.5,
        "Intensity": 1.26,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 692.4,
        "Intensity": 1.709,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 692.41,
        "Intensity": 0.149,
        "Nuclide": "Co-57 (EC 271.74 D)"
    },
    {
        "E(keV)": 692.425,
        "Intensity": 1.792,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 692.65,
        "Intensity": 3.852,
        "Nuclide": "Sb-122 (B- 2.7238 D)"
    },
    {
        "E(keV)": 693.4,
        "Intensity": 3.536,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 693.5,
        "Intensity": 14.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 693.783,
        "Intensity": 24.304,
        "Nuclide": "Es-254m (B- 39.3 H)"
    },
    {
        "E(keV)": 694.0,
        "Intensity": 0.546,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 694.0,
        "Intensity": 0.457,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 695.0,
        "Intensity": 99.6,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 695.0,
        "Intensity": 0.0002294,
        "Nuclide": "I-126 (EC 13.11 D)"
    },
    {
        "E(keV)": 695.6,
        "Intensity": 3.097,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 695.88,
        "Intensity": 3.071,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 696.49,
        "Intensity": 99.271,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 697.0,
        "Intensity": 28.884,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 697.2,
        "Intensity": 4.7,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 697.3,
        "Intensity": 6.281,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 697.49,
        "Intensity": 46.992,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 697.8,
        "Intensity": 0.0368,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 698.374,
        "Intensity": 28.487,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 698.5,
        "Intensity": 3.643,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 699.0,
        "Intensity": 2.5e-08,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 700.5,
        "Intensity": 3.05e-06,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 701.56,
        "Intensity": 1.283,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 701.6,
        "Intensity": 12,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 701.7,
        "Intensity": 0.02549,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 702.099,
        "Intensity": 3.653,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 702.2,
        "Intensity": 12.2,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 702.622,
        "Intensity": 97.902,
        "Nuclide": "Nb-94 (B- 2.03E+4 Y)"
    },
    {
        "E(keV)": 703.089,
        "Intensity": 3.578,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 703.11,
        "Intensity": 0.01058,
        "Nuclide": "Ga-67 (EC 3.2612 D)"
    },
    {
        "E(keV)": 703.45,
        "Intensity": 31.548,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 703.87,
        "Intensity": 0.005188,
        "Nuclide": "Ir-192 (EC 73.827 D)"
    },
    {
        "E(keV)": 704.774,
        "Intensity": 1.798,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 705.18,
        "Intensity": 8e-05,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 705.3,
        "Intensity": 0.0131,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 705.52,
        "Intensity": 0.005291,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 706.54,
        "Intensity": 0.004999,
        "Nuclide": "Co-57 (EC 271.74 D)"
    },
    {
        "E(keV)": 706.682,
        "Intensity": 16.328,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 706.8,
        "Intensity": 1.632,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 706.9,
        "Intensity": 7.9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 707.0,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 707.5,
        "Intensity": 8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 707.5,
        "Intensity": 0.099,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 708.0,
        "Intensity": 0.31,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 708.195,
        "Intensity": 0.192,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 708.42,
        "Intensity": 4.1e-07,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 708.7,
        "Intensity": 6,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 708.7,
        "Intensity": 6,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 709.32,
        "Intensity": 1.36,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 711.683,
        "Intensity": 55.321,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 712.205,
        "Intensity": 1.113,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 712.5,
        "Intensity": 0.391,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 712.598,
        "Intensity": 0.232,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 712.647,
        "Intensity": 1.13,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 712.843,
        "Intensity": 0.09282,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 713.48,
        "Intensity": 0.232,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 713.781,
        "Intensity": 2.287,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 715.3,
        "Intensity": 0.003996,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 715.8,
        "Intensity": 0.857,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 716.87,
        "Intensity": 0.0003195,
        "Nuclide": "Sr-85 (EC 64.84 D)"
    },
    {
        "E(keV)": 717.34,
        "Intensity": 29.375,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 717.424,
        "Intensity": 4.082,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 717.6,
        "Intensity": 8,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 717.72,
        "Intensity": 4.05,
        "Nuclide": "Pm-151 (B- 28.40 H)"
    },
    {
        "E(keV)": 719.5,
        "Intensity": 0.199,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 720.392,
        "Intensity": 12.178,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 720.5,
        "Intensity": 53.784,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 721.5,
        "Intensity": 0.119,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 721.929,
        "Intensity": 5.393,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 722.2,
        "Intensity": 1.877,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 722.78,
        "Intensity": 7.965,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 722.7842,
        "Intensity": 10.809,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 722.907,
        "Intensity": 90.84,
        "Nuclide": "Ag-108m (EC 418 Y)"
    },
    {
        "E(keV)": 722.911,
        "Intensity": 1.773,
        "Nuclide": "I-131 (B- 8.02070 D)"
    },
    {
        "E(keV)": 723.3,
        "Intensity": 4.3,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 723.305,
        "Intensity": 20.107,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 723.47,
        "Intensity": 5.418,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 724.199,
        "Intensity": 44.173,
        "Nuclide": "Zr-95 (B- 64.02 D)"
    },
    {
        "E(keV)": 725.24,
        "Intensity": 3.238,
        "Nuclide": "In-114m (EC 49.51 D)"
    },
    {
        "E(keV)": 725.673,
        "Intensity": 12.864,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 725.7,
        "Intensity": 32.703,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 725.7,
        "Intensity": 12.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 726.22,
        "Intensity": 3.692,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 728.2,
        "Intensity": 1.738,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 729.57,
        "Intensity": 0.717,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 729.6,
        "Intensity": 37,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 730.66,
        "Intensity": 5.263,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 731.6,
        "Intensity": 0.01207,
        "Nuclide": "Ca-47 (B- 4.536 D)"
    },
    {
        "E(keV)": 732.6,
        "Intensity": 14,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 733.8,
        "Intensity": 1,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 733.93,
        "Intensity": 0.06419,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 734.2,
        "Intensity": 0.001998,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 734.3,
        "Intensity": 3.335,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 734.4,
        "Intensity": 0.03943,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 735.93,
        "Intensity": 22.805,
        "Nuclide": "Pm-146 (EC 5.53 Y)"
    },
    {
        "E(keV)": 737.455,
        "Intensity": 9.852,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 738.6,
        "Intensity": 12.684,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 739.1,
        "Intensity": 0.0832,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 739.5,
        "Intensity": 12.13,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 739.58,
        "Intensity": 0.34,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 739.78,
        "Intensity": 47.7,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 740.96,
        "Intensity": 0.0279,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 741.355,
        "Intensity": 12.776,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 741.98,
        "Intensity": 38.5,
        "Nuclide": "Pm-143 (EC 265 D)"
    },
    {
        "E(keV)": 742.1,
        "Intensity": 1.2e-06,
        "Nuclide": "Pr-143 (B- 13.564 D)"
    },
    {
        "E(keV)": 742.2,
        "Intensity": 1.464e-06,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 742.78,
        "Intensity": 5.299,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 742.81,
        "Intensity": 5.2e-06,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 744.233,
        "Intensity": 63.479,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 744.277,
        "Intensity": 4.7,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 745.35,
        "Intensity": 102,
        "Nuclide": "Tc-98 (B- 4.2E+6 Y)"
    },
    {
        "E(keV)": 745.9,
        "Intensity": 0.207,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 747.159,
        "Intensity": 94.147,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 747.24,
        "Intensity": 33.993,
        "Nuclide": "Pm-146 (B- 5.53 Y)"
    },
    {
        "E(keV)": 748.057,
        "Intensity": 5.32,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 748.36,
        "Intensity": 20.919,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 748.6,
        "Intensity": 0.07529,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 748.601,
        "Intensity": 8.718,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 748.7,
        "Intensity": 37,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 749.46,
        "Intensity": 0.003233,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 749.895,
        "Intensity": 0.259,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 749.95,
        "Intensity": 50.129,
        "Nuclide": "Ni-56 (EC 6.075 D)"
    },
    {
        "E(keV)": 750.12,
        "Intensity": 0.442,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 751.068,
        "Intensity": 2.197,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 751.637,
        "Intensity": 4.331,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 752.285,
        "Intensity": 12.291,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 752.5,
        "Intensity": 8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 752.8,
        "Intensity": 2.718,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 753.819,
        "Intensity": 4.123,
        "Nuclide": "I-126 (EC 13.11 D)"
    },
    {
        "E(keV)": 753.99,
        "Intensity": 0.07529,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 754.6,
        "Intensity": 0.002672,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 755.35,
        "Intensity": 1.657,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 756.729,
        "Intensity": 54.46,
        "Nuclide": "Zr-95 (B- 64.02 D)"
    },
    {
        "E(keV)": 756.804,
        "Intensity": 4.542,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 757.0,
        "Intensity": 4.6,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 757.36,
        "Intensity": 0.06147,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 758.6,
        "Intensity": 1.274e-05,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 759.1,
        "Intensity": 0.509,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 759.1,
        "Intensity": 0.04424,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 762.3,
        "Intensity": 0.192,
        "Nuclide": "Ce-137m (EC 34.4 H)"
    },
    {
        "E(keV)": 762.65,
        "Intensity": 22.243,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 763.4,
        "Intensity": 1.224,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 763.4,
        "Intensity": 6,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 763.7,
        "Intensity": 5.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 763.944,
        "Intensity": 22.138,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 764.74,
        "Intensity": 1.663,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 764.9,
        "Intensity": 0.215,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 765.28,
        "Intensity": 2.14,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 765.3,
        "Intensity": 0.182,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 765.807,
        "Intensity": 99.81,
        "Nuclide": "Nb-95 (B- 34.975 D)"
    },
    {
        "E(keV)": 765.81,
        "Intensity": 11.502,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 766.37,
        "Intensity": 0.587,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 766.39,
        "Intensity": 2.2e-05,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 766.84,
        "Intensity": 36.312,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 767.1,
        "Intensity": 0.191,
        "Nuclide": "Ca-47 (B- 4.536 D)"
    },
    {
        "E(keV)": 767.47,
        "Intensity": 0.0327,
        "Nuclide": "Re-186 (B- 3.7183 D)"
    },
    {
        "E(keV)": 767.7,
        "Intensity": 5.436,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 768.77,
        "Intensity": 0.002886,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 768.93,
        "Intensity": 0.003637,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 769.778,
        "Intensity": 0.665,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 769.8,
        "Intensity": 8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 769.9,
        "Intensity": 5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 770.0,
        "Intensity": 0.0264,
        "Nuclide": "Cf-249 (A 351 Y)"
    },
    {
        "E(keV)": 770.6,
        "Intensity": 0.002958,
        "Nuclide": "Zn-65 (EC 244.26 D)"
    },
    {
        "E(keV)": 771.1,
        "Intensity": 1.159,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 771.2,
        "Intensity": 2.029,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 771.74,
        "Intensity": 0.122,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 772.6,
        "Intensity": 0.07186,
        "Nuclide": "Cs-132 (EC 6.479 D)"
    },
    {
        "E(keV)": 773.4,
        "Intensity": 4.662e-06,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 773.5,
        "Intensity": 2.2e-05,
        "Nuclide": "Re-186 (B- 3.7183 D)"
    },
    {
        "E(keV)": 773.67,
        "Intensity": 38.915,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 776.33,
        "Intensity": 4.432,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 776.517,
        "Intensity": 83.54,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 776.6,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 777.921,
        "Intensity": 4.258,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 778.04,
        "Intensity": 5.023,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 778.22,
        "Intensity": 99.271,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 778.44,
        "Intensity": 1.472,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 778.57,
        "Intensity": 1.509,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 778.817,
        "Intensity": 3.078,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 778.904,
        "Intensity": 12.942,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 780.183,
        "Intensity": 9.529,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 780.681,
        "Intensity": 4.35,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 781.2,
        "Intensity": 5.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 781.35,
        "Intensity": 1.36,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 782.49,
        "Intensity": 7.933,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 783.29,
        "Intensity": 16.995,
        "Nuclide": "V-50 (B- 1.4E+17 Y)"
    },
    {
        "E(keV)": 783.7,
        "Intensity": 15.125,
        "Nuclide": "Sb-127 (B- 3.85 D)"
    },
    {
        "E(keV)": 784.5,
        "Intensity": 1,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 785.05,
        "Intensity": 0.07187,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 785.1,
        "Intensity": 18.174,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 785.89,
        "Intensity": 0.0119,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 786.16,
        "Intensity": 0.01584,
        "Nuclide": "Nb-95m (B- 86.6 H)"
    },
    {
        "E(keV)": 786.198,
        "Intensity": 8.551,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 786.28,
        "Intensity": 3.207,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 786.3,
        "Intensity": 3.25e-06,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 786.44,
        "Intensity": 0.05426,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 787.1,
        "Intensity": 1.023,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 788.14,
        "Intensity": 0.262,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 788.742,
        "Intensity": 33.6,
        "Nuclide": "La-138 (B- 1.05E+11 Y)"
    },
    {
        "E(keV)": 788.876,
        "Intensity": 7.787,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 790.15,
        "Intensity": 0.68,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 790.711,
        "Intensity": 0.743,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 792.067,
        "Intensity": 3.692,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 792.067,
        "Intensity": 37.386,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 793.3,
        "Intensity": 0.01626,
        "Nuclide": "Sb-122 (B- 2.7238 D)"
    },
    {
        "E(keV)": 793.75,
        "Intensity": 14.13,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 794.386,
        "Intensity": 0.0539,
        "Nuclide": "Ga-67 (EC 3.2612 D)"
    },
    {
        "E(keV)": 795.864,
        "Intensity": 85.53,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 798.3,
        "Intensity": 4,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 798.7,
        "Intensity": 65.624,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 798.729,
        "Intensity": 4.84,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 799.37,
        "Intensity": 0.245,
        "Nuclide": "Rb-83 (EC 86.2 D)"
    },
    {
        "E(keV)": 800.0,
        "Intensity": 1.48,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 800.1,
        "Intensity": 4,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 800.28,
        "Intensity": 1.067,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 801.953,
        "Intensity": 8.69,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 803.1,
        "Intensity": 0.00121,
        "Nuclide": "Po-210 (A 138.376 D)"
    },
    {
        "E(keV)": 803.1,
        "Intensity": 100.638,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 803.25,
        "Intensity": 0.07533,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 804.28,
        "Intensity": 12.551,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 804.8,
        "Intensity": 0.389,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 805.7,
        "Intensity": 4.041e-05,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 806.372,
        "Intensity": 9.611,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 807.25,
        "Intensity": 0.994,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 807.38,
        "Intensity": 22.692,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 807.46,
        "Intensity": 1.196,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 807.8,
        "Intensity": 1.208,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 807.86,
        "Intensity": 6.248,
        "Nuclide": "Ca-47 (B- 4.536 D)"
    },
    {
        "E(keV)": 808.11,
        "Intensity": 0.01643,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 808.2,
        "Intensity": 25,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 808.25,
        "Intensity": 8e-07,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 810.064,
        "Intensity": 17.032,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 810.276,
        "Intensity": 58.08,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 810.775,
        "Intensity": 84.632,
        "Nuclide": "Co-58 (EC 70.86 D)"
    },
    {
        "E(keV)": 811.77,
        "Intensity": 9.7,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 811.85,
        "Intensity": 87.093,
        "Nuclide": "Ni-56 (EC 6.075 D)"
    },
    {
        "E(keV)": 812.54,
        "Intensity": 81.601,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 814.14,
        "Intensity": 0.546,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 815.772,
        "Intensity": 23.278,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 815.989,
        "Intensity": 50.833,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 817.0,
        "Intensity": 7.77e-07,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 817.04,
        "Intensity": 0.09331,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 817.79,
        "Intensity": 2.066,
        "Nuclide": "Br-77 (EC 57.036 H)"
    },
    {
        "E(keV)": 817.8,
        "Intensity": 6.37e-05,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 818.031,
        "Intensity": 7.295,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 818.1,
        "Intensity": 0.74,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 818.514,
        "Intensity": 99.704,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 819.187,
        "Intensity": 7.454,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 819.29,
        "Intensity": 0.623,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 820.61,
        "Intensity": 0.0003727,
        "Nuclide": "Nb-95m (B- 86.6 H)"
    },
    {
        "E(keV)": 820.624,
        "Intensity": 4.654,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 821.162,
        "Intensity": 11.961,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 821.8,
        "Intensity": 0.345,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 822.48,
        "Intensity": 4.278,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 822.78,
        "Intensity": 6.236,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 822.972,
        "Intensity": 0.133,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 824.6,
        "Intensity": 3.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 824.69,
        "Intensity": 15.578,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 824.82,
        "Intensity": 0.441,
        "Nuclide": "Ce-137m (EC 34.4 H)"
    },
    {
        "E(keV)": 826.28,
        "Intensity": 0.0076,
        "Nuclide": "Co-60 (B- 5.2714 Y)"
    },
    {
        "E(keV)": 827.828,
        "Intensity": 24.034,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 828.32,
        "Intensity": 10.753,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 828.5,
        "Intensity": 0.42,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 828.99,
        "Intensity": 3.381,
        "Nuclide": "Ir-190 (EC 11.78 D)"
    },
    {
        "E(keV)": 829.42,
        "Intensity": 5.4,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 829.948,
        "Intensity": 6.959,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 830.53,
        "Intensity": 0.03255,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 830.577,
        "Intensity": 9.816,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 831.0,
        "Intensity": 7.77e-07,
        "Nuclide": "U-232 (A 68.9 Y)"
    },
    {
        "E(keV)": 831.2,
        "Intensity": 6,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 831.97,
        "Intensity": 1.173,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 832.0,
        "Intensity": 1.464e-05,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 833.4,
        "Intensity": 0.03317,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 833.5,
        "Intensity": 5.379,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 833.99,
        "Intensity": 9.62,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 834.848,
        "Intensity": 99.976,
        "Nuclide": "Mn-54 (EC 312.12 D)"
    },
    {
        "E(keV)": 835.13,
        "Intensity": 2.563e-05,
        "Nuclide": "Nb-95m (B- 86.6 H)"
    },
    {
        "E(keV)": 835.149,
        "Intensity": 26.297,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 835.38,
        "Intensity": 0.103,
        "Nuclide": "Ce-137m (EC 34.4 H)"
    },
    {
        "E(keV)": 835.43,
        "Intensity": 1.044,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 839.943,
        "Intensity": 3.034,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 840.2,
        "Intensity": 4.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 843.8,
        "Intensity": 6.8,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 844.1,
        "Intensity": 0.01124,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 844.8,
        "Intensity": 0.141,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 844.81,
        "Intensity": 0.03511,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 846.2,
        "Intensity": 0.844,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 846.771,
        "Intensity": 80.928,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 847.0,
        "Intensity": 0.0002994,
        "Nuclide": "Cs-134 (EC 2.0648 Y)"
    },
    {
        "E(keV)": 847.4,
        "Intensity": 0.02722,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 848.18,
        "Intensity": 2.342,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 849.86,
        "Intensity": 97.087,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 849.9,
        "Intensity": 0.152,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 850.6,
        "Intensity": 0.06536,
        "Nuclide": "Y-88 (B+ 106.65 D)"
    },
    {
        "E(keV)": 851.7,
        "Intensity": 1.25e-06,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 852.21,
        "Intensity": 21.036,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 852.6,
        "Intensity": 0.02061,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 853.05,
        "Intensity": 0.264,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 853.051,
        "Intensity": 2.542,
        "Nuclide": "Lu-171 (EC 8.24 D)"
    },
    {
        "E(keV)": 855.44,
        "Intensity": 0.04278,
        "Nuclide": "Ru-97 (EC 2.9 D)"
    },
    {
        "E(keV)": 856.245,
        "Intensity": 0.0022,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 856.7,
        "Intensity": 17.629,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 856.929,
        "Intensity": 2.698,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 857.5,
        "Intensity": 5.39e-06,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 859.46,
        "Intensity": 0.108,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 860.93,
        "Intensity": 3.54,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 861.7,
        "Intensity": 0.0004189,
        "Nuclide": "Po-208 (EC 2.898 Y)"
    },
    {
        "E(keV)": 863.89,
        "Intensity": 1.936,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 863.959,
        "Intensity": 0.581,
        "Nuclide": "Co-58 (EC 70.86 D)"
    },
    {
        "E(keV)": 864.6,
        "Intensity": 3.2,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 865.1,
        "Intensity": 0.001536,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 866.76,
        "Intensity": 5.808,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 867.0,
        "Intensity": 0.003607,
        "Nuclide": "Ag-111 (B- 7.45 D)"
    },
    {
        "E(keV)": 867.2,
        "Intensity": 0.002564,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 867.373,
        "Intensity": 4.253,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 867.64,
        "Intensity": 0.131,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 867.846,
        "Intensity": 5.505,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 868.06,
        "Intensity": 0.01248,
        "Nuclide": "Sr-85 (EC 64.84 D)"
    },
    {
        "E(keV)": 869.256,
        "Intensity": 1.901,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 869.891,
        "Intensity": 5.577,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 871.091,
        "Intensity": 99.9,
        "Nuclide": "Nb-94 (B- 2.03E+4 Y)"
    },
    {
        "E(keV)": 871.98,
        "Intensity": 9.09,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 873.1,
        "Intensity": 4,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 873.19,
        "Intensity": 12.202,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 873.92,
        "Intensity": 5.8e-07,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 874.18,
        "Intensity": 0.235,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 874.813,
        "Intensity": 6.522,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 879.383,
        "Intensity": 30.1,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 879.876,
        "Intensity": 0.754,
        "Nuclide": "I-126 (B- 13.11 D)"
    },
    {
        "E(keV)": 880.46,
        "Intensity": 1.031,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 880.523,
        "Intensity": 5.359,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 881.01,
        "Intensity": 67.327,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 881.6041,
        "Intensity": 50.566,
        "Nuclide": "Rb-84 (EC 32.77 D)"
    },
    {
        "E(keV)": 881.98,
        "Intensity": 0.02387,
        "Nuclide": "Pm-149 (B- 53.08 H)"
    },
    {
        "E(keV)": 882.63,
        "Intensity": 0.87,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 883.23,
        "Intensity": 7.7e-07,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 884.5,
        "Intensity": 4.9,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 884.5365,
        "Intensity": 0.291,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 884.685,
        "Intensity": 72.195,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 886.15,
        "Intensity": 2.012,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 887.0,
        "Intensity": 0.01432,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 887.693,
        "Intensity": 0.149,
        "Nuclide": "Ga-67 (EC 3.2612 D)"
    },
    {
        "E(keV)": 888.8,
        "Intensity": 26.393,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 889.277,
        "Intensity": 99.984,
        "Nuclide": "Sc-46 (B- 83.810 D)"
    },
    {
        "E(keV)": 889.753,
        "Intensity": 5.89,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 890.1,
        "Intensity": 0.03971,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 893.4,
        "Intensity": 0.291,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 893.5,
        "Intensity": 8.23,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 893.73,
        "Intensity": 64.971,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 894.26,
        "Intensity": 0.0938,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 894.351,
        "Intensity": 19.844,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 894.7,
        "Intensity": 1.666e-06,
        "Nuclide": "Cm-244 (A 18.10 Y)"
    },
    {
        "E(keV)": 894.76,
        "Intensity": 2.75,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 894.76,
        "Intensity": 15.557,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 895.0,
        "Intensity": 13,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 895.12,
        "Intensity": 15.931,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 896.42,
        "Intensity": 0.981,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 896.6,
        "Intensity": 0.47,
        "Nuclide": "Po-209 (EC 102 Y)"
    },
    {
        "E(keV)": 896.9,
        "Intensity": 0.696,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 897.33,
        "Intensity": 2.2e-05,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 897.549,
        "Intensity": 0.09616,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 897.622,
        "Intensity": 0.144,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 897.8,
        "Intensity": 0.121,
        "Nuclide": "Bi-207 (EC 31.55 Y)"
    },
    {
        "E(keV)": 898.042,
        "Intensity": 93.489,
        "Nuclide": "Y-88 (B+ 106.65 D)"
    },
    {
        "E(keV)": 898.68,
        "Intensity": 5.341,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 899.9,
        "Intensity": 0.0368,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 900.724,
        "Intensity": 30.542,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 900.797,
        "Intensity": 2.815,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 903.282,
        "Intensity": 3.735,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 903.282,
        "Intensity": 37.804,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 903.94,
        "Intensity": 0.04218,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 904.076,
        "Intensity": 0.893,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 906.425,
        "Intensity": 0.219,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 906.84,
        "Intensity": 0.002778,
        "Nuclide": "Ce-137m (EC 34.4 H)"
    },
    {
        "E(keV)": 906.98,
        "Intensity": 0.03455,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 908.1,
        "Intensity": 1.708e-06,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 908.4,
        "Intensity": 3.6,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 908.96,
        "Intensity": 0.00956,
        "Nuclide": "Sr-89 (B- 50.53 D)"
    },
    {
        "E(keV)": 909.15,
        "Intensity": 76.515,
        "Nuclide": "Zr-89 (EC 78.41 H)"
    },
    {
        "E(keV)": 909.847,
        "Intensity": 0.07028,
        "Nuclide": "Te-121m (EC 154 D)"
    },
    {
        "E(keV)": 910.0,
        "Intensity": 3.355,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 910.9,
        "Intensity": 1.666,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 912.064,
        "Intensity": 1.416,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 912.079,
        "Intensity": 15.623,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 912.6,
        "Intensity": 1.783,
        "Nuclide": "Nb-92m (EC 10.15 D)"
    },
    {
        "E(keV)": 912.6,
        "Intensity": 6.168,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 914.85,
        "Intensity": 11.455,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 914.933,
        "Intensity": 3.11,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 915.33,
        "Intensity": 17.096,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 915.55,
        "Intensity": 4.132,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 915.6,
        "Intensity": 0.315,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 915.8,
        "Intensity": 100,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 916.1,
        "Intensity": 0.09148,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 917.45,
        "Intensity": 0.01279,
        "Nuclide": "Ce-137m (EC 34.4 H)"
    },
    {
        "E(keV)": 918.48,
        "Intensity": 7.558,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 918.69,
        "Intensity": 0.59,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 918.7,
        "Intensity": 5.4e-07,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 919.33,
        "Intensity": 0.427,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 919.55,
        "Intensity": 2.662,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 920.553,
        "Intensity": 0.217,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 920.933,
        "Intensity": 8.136,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 923.87,
        "Intensity": 0.721,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 923.98,
        "Intensity": 2.86,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 924.1,
        "Intensity": 2.389,
        "Nuclide": "Es-252 (EC 471.7 D)"
    },
    {
        "E(keV)": 925.189,
        "Intensity": 6.897,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 925.56,
        "Intensity": 0.04415,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 925.68,
        "Intensity": 3.41,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 926.72,
        "Intensity": 5.8e-07,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 928.327,
        "Intensity": 0.387,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 929.01,
        "Intensity": 20.471,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 929.106,
        "Intensity": 3.118,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 930.58,
        "Intensity": 0.07293,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 931.057,
        "Intensity": 0.05011,
        "Nuclide": "Os-185 (EC 93.6 D)"
    },
    {
        "E(keV)": 931.7,
        "Intensity": 3,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 932.6,
        "Intensity": 1.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 932.96,
        "Intensity": 0.659,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 933.005,
        "Intensity": 3.439,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 933.838,
        "Intensity": 2,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 934.44,
        "Intensity": 99.065,
        "Nuclide": "Nb-92m (EC 10.15 D)"
    },
    {
        "E(keV)": 934.5,
        "Intensity": 100,
        "Nuclide": "Nb-92 (EC 3.47E7 Y)"
    },
    {
        "E(keV)": 934.6,
        "Intensity": 0.02629,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 934.63,
        "Intensity": 0.209,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 935.544,
        "Intensity": 66.653,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 936.61,
        "Intensity": 0.4,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 937.493,
        "Intensity": 34.133,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 938.0,
        "Intensity": 0.0004018,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 938.61,
        "Intensity": 2.536,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 940.4,
        "Intensity": 1.127,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 941.38,
        "Intensity": 0.54,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 941.9,
        "Intensity": 4.7e-07,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 942.21,
        "Intensity": 5.024,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 944.132,
        "Intensity": 3.897,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 944.189,
        "Intensity": 43.709,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 944.8,
        "Intensity": 0.05539,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 945.91,
        "Intensity": 0.434,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 946.046,
        "Intensity": 0.0692,
        "Nuclide": "Cs-129 (EC 32.06 H)"
    },
    {
        "E(keV)": 946.989,
        "Intensity": 0.008217,
        "Nuclide": "Te-121m (EC 154 D)"
    },
    {
        "E(keV)": 947.835,
        "Intensity": 1.018,
        "Nuclide": "Gd-149 (EC 9.28 D)"
    },
    {
        "E(keV)": 948.29,
        "Intensity": 2.201,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 950.967,
        "Intensity": 2.755,
        "Nuclide": "Ho-166m (B- 1.20E3 Y)"
    },
    {
        "E(keV)": 950.99,
        "Intensity": 0.519,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 951.0,
        "Intensity": 2.996e-05,
        "Nuclide": "Sr-85 (EC 64.84 D)"
    },
    {
        "E(keV)": 951.19,
        "Intensity": 0.00028,
        "Nuclide": "Cd-115 (B- 53.46 H)"
    },
    {
        "E(keV)": 951.95,
        "Intensity": 26.705,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 955.832,
        "Intensity": 3.835,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 956.4,
        "Intensity": 1.461,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 958.0,
        "Intensity": 1e-07,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 959.3,
        "Intensity": 0.03891,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 959.7,
        "Intensity": 0.06854,
        "Nuclide": "Tl-202 (EC 12.23 D)"
    },
    {
        "E(keV)": 960.0,
        "Intensity": 5e-08,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 960.622,
        "Intensity": 25.721,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 960.754,
        "Intensity": 0.09461,
        "Nuclide": "Mo-99 (B- 65.94 H)"
    },
    {
        "E(keV)": 961.92,
        "Intensity": 0.209,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 962.126,
        "Intensity": 20.193,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 962.317,
        "Intensity": 9.813,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 962.77,
        "Intensity": 0.7,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 964.079,
        "Intensity": 14.632,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 964.11,
        "Intensity": 0.342,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 966.171,
        "Intensity": 25.103,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 966.9,
        "Intensity": 4,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 967.0,
        "Intensity": 5e-08,
        "Nuclide": "Pu-240 (A 6564 Y)"
    },
    {
        "E(keV)": 967.306,
        "Intensity": 2.748,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 968.199,
        "Intensity": 1.892,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 968.22,
        "Intensity": 0.335,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 969.315,
        "Intensity": 41.624,
        "Nuclide": "Pa-232 (B- 1.31 D)"
    },
    {
        "E(keV)": 976.37,
        "Intensity": 2.679,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 977.131,
        "Intensity": 0.174,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 977.373,
        "Intensity": 1.173,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 979.29,
        "Intensity": 2.973,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 980.23,
        "Intensity": 7.08,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 982.2,
        "Intensity": 0.237,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 983.521,
        "Intensity": 50.221,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 983.526,
        "Intensity": 100.11,
        "Nuclide": "Sc-48 (B- 43.67 H)"
    },
    {
        "E(keV)": 984.45,
        "Intensity": 27.8,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 984.5,
        "Intensity": 2e-06,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 985.1,
        "Intensity": 5.371,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 986.0,
        "Intensity": 0.28,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 987.66,
        "Intensity": 16.367,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 987.76,
        "Intensity": 76.97,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 989.3,
        "Intensity": 6.773,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 991.78,
        "Intensity": 1.063,
        "Nuclide": "Tb-153 (EC 2.34 D)"
    },
    {
        "E(keV)": 992.077,
        "Intensity": 0.546,
        "Nuclide": "Lu-174m (EC 142 D)"
    },
    {
        "E(keV)": 992.9,
        "Intensity": 1.464e-06,
        "Nuclide": "Th-228 (A 1.912 Y)"
    },
    {
        "E(keV)": 993.46,
        "Intensity": 0.01032,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 993.81,
        "Intensity": 0.001985,
        "Nuclide": "Ce-137m (EC 34.4 H)"
    },
    {
        "E(keV)": 994.1,
        "Intensity": 4.5,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 994.2,
        "Intensity": 0.443,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 996.262,
        "Intensity": 10.533,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 998.291,
        "Intensity": 0.07953,
        "Nuclide": "Te-121m (EC 154 D)"
    },
    {
        "E(keV)": 998.7,
        "Intensity": 0.696,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 1001.03,
        "Intensity": 9.9e-07,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 1001.05,
        "Intensity": 1.599,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 1001.695,
        "Intensity": 2.066,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 1001.85,
        "Intensity": 1.2,
        "Nuclide": "Sc-44m (EC 58.6 H)"
    },
    {
        "E(keV)": 1002.74,
        "Intensity": 5.378,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 1002.85,
        "Intensity": 0.07533,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 1002.88,
        "Intensity": 1.038,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 1003.2,
        "Intensity": 3.446,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 1004.49,
        "Intensity": 0.02249,
        "Nuclide": "Ce-137m (EC 34.4 H)"
    },
    {
        "E(keV)": 1004.725,
        "Intensity": 17.906,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 1005.272,
        "Intensity": 0.647,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 1005.7,
        "Intensity": 0.002689,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 1007.15,
        "Intensity": 3.063,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 1007.47,
        "Intensity": 1.983,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 1007.59,
        "Intensity": 1.271,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 1009.6,
        "Intensity": 0.993,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 1010.0,
        "Intensity": 4e-06,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 1010.24,
        "Intensity": 0.09116,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 1011.8,
        "Intensity": 3.6,
        "Nuclide": "Ir-194m (B- 171 D)"
    },
    {
        "E(keV)": 1013.2,
        "Intensity": 2.47,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 1013.2,
        "Intensity": 2.47,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 1013.81,
        "Intensity": 20.198,
        "Nuclide": "Pm-148m (B- 41.29 D)"
    },
    {
        "E(keV)": 1013.9,
        "Intensity": 3.7,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 1016.158,
        "Intensity": 0.256,
        "Nuclide": "Rb-84 (EC 32.77 D)"
    },
    {
        "E(keV)": 1017.4,
        "Intensity": 0.32,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 1018.63,
        "Intensity": 7.729,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 1021.0,
        "Intensity": 0.001926,
        "Nuclide": "Sn-123 (B- 129.2 D)"
    },
    {
        "E(keV)": 1021.8,
        "Intensity": 0.263,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 1022.43,
        "Intensity": 0.0178,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 1022.63,
        "Intensity": 0.514,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 1023.3,
        "Intensity": 99.4,
        "Nuclide": "Sb-120 (EC 5.76 D)"
    },
    {
        "E(keV)": 1023.4,
        "Intensity": 0.161,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 1024.0,
        "Intensity": 7.977e-05,
        "Nuclide": "Te-121m (EC 154 D)"
    },
    {
        "E(keV)": 1025.87,
        "Intensity": 9.6,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 1026.05,
        "Intensity": 1.34,
        "Nuclide": "Pa-230 (EC 17.4 D)"
    },
    {
        "E(keV)": 1026.512,
        "Intensity": 0.223,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 1028.5,
        "Intensity": 1.6e-06,
        "Nuclide": "Cm-242 (A 162.8 D)"
    },
    {
        "E(keV)": 1028.54,
        "Intensity": 20.3,
        "Nuclide": "Np-238 (B- 2.117 D)"
    },
    {
        "E(keV)": 1030.23,
        "Intensity": 0.03102,
        "Nuclide": "Sn-123 (B- 129.2 D)"
    },
    {
        "E(keV)": 1031.66,
        "Intensity": 0.125,
        "Nuclide": "Cs-132 (B- 6.479 D)"
    },
    {
        "E(keV)": 1032.26,
        "Intensity": 32.903,
        "Nuclide": "Po-206 (EC 8.8 D)"
    },
    {
        "E(keV)": 1033.986,
        "Intensity": 7.894,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 1035.4,
        "Intensity": 0.0005584,
        "Nuclide": "Te-121m (EC 154 D)"
    },
    {
        "E(keV)": 1036.0,
        "Intensity": 1.883,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 1037.522,
        "Intensity": 97.607,
        "Nuclide": "Sc-48 (B- 43.67 H)"
    },
    {
        "E(keV)": 1037.84,
        "Intensity": 11.475,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 1038.61,
        "Intensity": 0.988,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 1039.264,
        "Intensity": 2.742,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 1039.3,
        "Intensity": 6.1,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 1040.7,
        "Intensity": 5,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 1041.8,
        "Intensity": 2.2e-07,
        "Nuclide": "Pu-238 (A 87.7 Y)"
    },
    {
        "E(keV)": 1043.75,
        "Intensity": 7.619,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 1044.002,
        "Intensity": 27.234,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 1045.0,
        "Intensity": 0.339,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 1045.128,
        "Intensity": 1.841,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 1045.75,
        "Intensity": 0.04937,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 1045.83,
        "Intensity": 29.998,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 1046.59,
        "Intensity": 36.312,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 1046.59,
        "Intensity": 0.276,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 1046.68,
        "Intensity": 0.07555,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 1047.6,
        "Intensity": 1.325,
        "Nuclide": "Ba-131 (EC 11.50 D)"
    },
    {
        "E(keV)": 1048.073,
        "Intensity": 79.763,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 1048.44,
        "Intensity": 3.149,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 1049.043,
        "Intensity": 5.517,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 1050.21,
        "Intensity": 0.01828,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 1050.75,
        "Intensity": 0.119,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 1052.02,
        "Intensity": 0.328,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 1054.28,
        "Intensity": 4.61,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 1054.3,
        "Intensity": 5.8,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 1056.79,
        "Intensity": 0.008745,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 1057.62,
        "Intensity": 2.165,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 1057.8,
        "Intensity": 0.291,
        "Nuclide": "Ta-177 (EC 56.56 H)"
    },
    {
        "E(keV)": 1058.71,
        "Intensity": 3.766,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 1060.28,
        "Intensity": 2.099,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 1061.48,
        "Intensity": 0.053,
        "Nuclide": "Ir-192 (B- 73.827 D)"
    },
    {
        "E(keV)": 1062.0,
        "Intensity": 0.367,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 1062.0,
        "Intensity": 3.12,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 1063.662,
        "Intensity": 74.507,
        "Nuclide": "Bi-207 (EC 31.55 Y)"
    },
    {
        "E(keV)": 1063.9,
        "Intensity": 0.002511,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 1065.04,
        "Intensity": 0.0164,
        "Nuclide": "Lu-174 (EC 3.31 Y)"
    },
    {
        "E(keV)": 1065.11,
        "Intensity": 10.772,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 1065.14,
        "Intensity": 4.922,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 1067.1,
        "Intensity": 9.7,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 1069.35,
        "Intensity": 7.281,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 1076.15,
        "Intensity": 0.792,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 1076.2,
        "Intensity": 10.427,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 1077.0,
        "Intensity": 8.64,
        "Nuclide": "Rb-86 (B- 18.631 D)"
    },
    {
        "E(keV)": 1077.043,
        "Intensity": 6.137,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 1078.8,
        "Intensity": 3.98,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 1078.91,
        "Intensity": 0.429,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 1079.16,
        "Intensity": 4.589,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 1081.29,
        "Intensity": 0.618,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 1081.35,
        "Intensity": 1.575,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 1081.4,
        "Intensity": 6.24,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 1085.2,
        "Intensity": 0.409,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 1085.869,
        "Intensity": 10.226,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 1087.684,
        "Intensity": 0.159,
        "Nuclide": "Au-198 (B- 2.69517 D)"
    },
    {
        "E(keV)": 1087.7,
        "Intensity": 1.193,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 1087.94,
        "Intensity": 3.986,
        "Nuclide": "Ag-105 (EC 41.29 D)"
    },
    {
        "E(keV)": 1088.64,
        "Intensity": 0.6,
        "Nuclide": "Sn-123 (B- 129.2 D)"
    },
    {
        "E(keV)": 1089.15,
        "Intensity": 4.588,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 1089.737,
        "Intensity": 1.727,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 1090.2,
        "Intensity": 14,
        "Nuclide": "Pu-242 (SF 3.733E+5 Y)"
    },
    {
        "E(keV)": 1091.3,
        "Intensity": 1.092,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 1091.4,
        "Intensity": 0.148,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 1093.59,
        "Intensity": 6,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 1093.63,
        "Intensity": 64.029,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 1095.49,
        "Intensity": 2.919,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 1095.75,
        "Intensity": 2.208,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 1098.26,
        "Intensity": 13.737,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 1099.251,
        "Intensity": 56.5,
        "Nuclide": "Fe-59 (B- 44.503 D)"
    },
    {
        "E(keV)": 1100.5,
        "Intensity": 8.4e-05,
        "Nuclide": "Sn-123 (B- 129.2 D)"
    },
    {
        "E(keV)": 1101.1,
        "Intensity": 0.003996,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 1102.149,
        "Intensity": 2.537,
        "Nuclide": "Te-121m (EC 154 D)"
    },
    {
        "E(keV)": 1103.16,
        "Intensity": 4.913,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 1103.16,
        "Intensity": 1.862,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 1103.25,
        "Intensity": 0.415,
        "Nuclide": "Ce-143 (B- 33.10 H)"
    },
    {
        "E(keV)": 1104.06,
        "Intensity": 2.018,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 1105.7,
        "Intensity": 0.25,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 1106.77,
        "Intensity": 27.545,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 1107.6,
        "Intensity": 0.0003989,
        "Nuclide": "Te-121m (EC 154 D)"
    },
    {
        "E(keV)": 1107.626,
        "Intensity": 2.137,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 1109.174,
        "Intensity": 0.186,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 1112.069,
        "Intensity": 13.669,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 1112.84,
        "Intensity": 20.292,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 1113.4,
        "Intensity": 0.821,
        "Nuclide": "Sb-120 (EC 5.76 D)"
    },
    {
        "E(keV)": 1113.88,
        "Intensity": 0.0222,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 1115.1,
        "Intensity": 0.347,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 1115.12,
        "Intensity": 1.565,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 1115.546,
        "Intensity": 49.892,
        "Nuclide": "Zn-65 (EC 244.26 D)"
    },
    {
        "E(keV)": 1120.545,
        "Intensity": 99.987,
        "Nuclide": "Sc-46 (B- 83.810 D)"
    },
    {
        "E(keV)": 1121.3,
        "Intensity": 21.745,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 1121.3008,
        "Intensity": 34.9,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 1121.44,
        "Intensity": 0.03513,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 1122.64,
        "Intensity": 0.409,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 1124.3,
        "Intensity": 4.734,
        "Nuclide": "Bk-246 (EC 1.80 D)"
    },
    {
        "E(keV)": 1125.46,
        "Intensity": 11.643,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 1126.08,
        "Intensity": 1.2,
        "Nuclide": "Sc-44m (EC 58.6 H)"
    },
    {
        "E(keV)": 1126.85,
        "Intensity": 15.089,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 1128.02,
        "Intensity": 11.928,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 1129.67,
        "Intensity": 0.456,
        "Nuclide": "Al-26 (EC 7.17E5 Y)"
    },
    {
        "E(keV)": 1129.87,
        "Intensity": 0.126,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 1130.9,
        "Intensity": 6.542,
        "Nuclide": "Gd-147 (EC 38.1 H)"
    },
    {
        "E(keV)": 1131.262,
        "Intensity": 1.743,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 1132.17,
        "Intensity": 0.005151,
        "Nuclide": "Nb-92m (EC 10.15 D)"
    },
    {
        "E(keV)": 1132.573,
        "Intensity": 0.0856,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 1135.1,
        "Intensity": 0.05152,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 1136.0,
        "Intensity": 0.474,
        "Nuclide": "Cs-132 (EC 6.479 D)"
    },
    {
        "E(keV)": 1136.75,
        "Intensity": 7.56,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 1138.65,
        "Intensity": 3.491,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 1139.461,
        "Intensity": 0.571,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 1140.67,
        "Intensity": 0.763,
        "Nuclide": "Sb-122 (EC 2.7209 D)"
    },
    {
        "E(keV)": 1144.65,
        "Intensity": 0.001077,
        "Nuclide": "Te-121m (EC 154 D)"
    },
    {
        "E(keV)": 1146.97,
        "Intensity": 0.01207,
        "Nuclide": "Ca-47 (B- 4.536 D)"
    },
    {
        "E(keV)": 1147.33,
        "Intensity": 0.952,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 1150.626,
        "Intensity": 2.024,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 1153.67,
        "Intensity": 6.79,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 1154.07,
        "Intensity": 10.373,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 1154.08,
        "Intensity": 4.734,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 1157.031,
        "Intensity": 1.2,
        "Nuclide": "Sc-44m (EC 58.6 H)"
    },
    {
        "E(keV)": 1158.1,
        "Intensity": 0.372,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 1159.03,
        "Intensity": 7.248,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 1159.97,
        "Intensity": 1.099,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 1167.968,
        "Intensity": 1.789,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 1170.587,
        "Intensity": 1.369,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 1171.7,
        "Intensity": 100,
        "Nuclide": "Sb-120 (EC 5.76 D)"
    },
    {
        "E(keV)": 1173.237,
        "Intensity": 99.974,
        "Nuclide": "Co-60 (B- 5.2714 Y)"
    },
    {
        "E(keV)": 1173.77,
        "Intensity": 1.213,
        "Nuclide": "Re-184m (EC 169 D)"
    },
    {
        "E(keV)": 1175.102,
        "Intensity": 1.853,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 1175.34,
        "Intensity": 2.018,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 1177.06,
        "Intensity": 0.000228,
        "Nuclide": "Sn-123 (B- 129.2 D)"
    },
    {
        "E(keV)": 1177.962,
        "Intensity": 14.869,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 1181.23,
        "Intensity": 0.000294,
        "Nuclide": "Sn-123 (B- 129.2 D)"
    },
    {
        "E(keV)": 1184.446,
        "Intensity": 2.977,
        "Nuclide": "Tm-165 (EC 30.06 H)"
    },
    {
        "E(keV)": 1184.88,
        "Intensity": 2.444,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 1187.143,
        "Intensity": 1.678,
        "Nuclide": "Tb-158 (EC 180 Y)"
    },
    {
        "E(keV)": 1188.0,
        "Intensity": 0.00424,
        "Nuclide": "Sb-122 (B- 2.7238 D)"
    },
    {
        "E(keV)": 1189.0,
        "Intensity": 8.927,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 1189.0503,
        "Intensity": 16.225,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 1190.03,
        "Intensity": 2.294,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 1193.78,
        "Intensity": 6.053,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 1196.858,
        "Intensity": 0.259,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 1197.108,
        "Intensity": 1.162,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 1199.39,
        "Intensity": 11.394,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 1199.89,
        "Intensity": 2.384,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 1200.1,
        "Intensity": 0.105,
        "Nuclide": "Cm-248 (SF 3.48E+5 Y)"
    },
    {
        "E(keV)": 1200.17,
        "Intensity": 0.367,
        "Nuclide": "Tc-96 (EC 4.28 D)"
    },
    {
        "E(keV)": 1204.35,
        "Intensity": 0.16,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 1204.67,
        "Intensity": 2.032,
        "Nuclide": "Nb-91m (EC 60.86 D)"
    },
    {
        "E(keV)": 1204.77,
        "Intensity": 0.26,
        "Nuclide": "Y-91 (B- 58.51 D)"
    },
    {
        "E(keV)": 1205.7,
        "Intensity": 29.744,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 1206.6,
        "Intensity": 9.946,
        "Nuclide": "Te-131m (B- 30 H)"
    },
    {
        "E(keV)": 1206.8,
        "Intensity": 0.0004589,
        "Nuclide": "I-126 (EC 13.11 D)"
    },
    {
        "E(keV)": 1207.21,
        "Intensity": 0.3,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 1209.77,
        "Intensity": 7.272,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 1212.496,
        "Intensity": 0.199,
        "Nuclide": "As-71 (EC 65.28 H)"
    },
    {
        "E(keV)": 1212.73,
        "Intensity": 65.338,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 1212.88,
        "Intensity": 2.383,
        "Nuclide": "Sc-48 (B- 43.67 H)"
    },
    {
        "E(keV)": 1212.92,
        "Intensity": 1.44,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 1212.948,
        "Intensity": 1.425,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 1213.0,
        "Intensity": 2.39,
        "Nuclide": "Sb-126 (B- 12.46 D)"
    },
    {
        "E(keV)": 1216.08,
        "Intensity": 3.42,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 1219.2,
        "Intensity": 0.0368,
        "Nuclide": "Am-240 (EC 50.8 H)"
    },
    {
        "E(keV)": 1220.88,
        "Intensity": 0.268,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 1221.0,
        "Intensity": 530,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 1221.4,
        "Intensity": 17.218,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 1221.4066,
        "Intensity": 26.978,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 1222.0,
        "Intensity": 0.008245,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 1222.44,
        "Intensity": 31,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 1222.5,
        "Intensity": 100,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 1222.88,
        "Intensity": 7.121,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 1224.0,
        "Intensity": 0.03547,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 1225.5,
        "Intensity": 3.339,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 1225.65,
        "Intensity": 4.834,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 1228.52,
        "Intensity": 1.215,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 1230.71,
        "Intensity": 7.983,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 1231.0,
        "Intensity": 14.725,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 1231.0157,
        "Intensity": 11.44,
        "Nuclide": "Ta-182 (B- 114.43 D)"
    },
    {
        "E(keV)": 1235.362,
        "Intensity": 20.041,
        "Nuclide": "Cs-136 (B- 13.16 D)"
    },
    {
        "E(keV)": 1237.22,
        "Intensity": 2.312,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 1238.282,
        "Intensity": 54.176,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 1241.17,
        "Intensity": 0.62,
        "Nuclide": "Hg-195m (EC 41.6 H)"
    },
    {
        "E(keV)": 1241.847,
        "Intensity": 5.125,
        "Nuclide": "Lu-174 (EC 3.31 Y)"
    },
    {
        "E(keV)": 1242.42,
        "Intensity": 6.601,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 1246.15,
        "Intensity": 0.864,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 1246.278,
        "Intensity": 2.969,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 1246.968,
        "Intensity": 1.96,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 1247.88,
        "Intensity": 0.268,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 1255.93,
        "Intensity": 0.907,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 1256.93,
        "Intensity": 0.813,
        "Nuclide": "Sb-122 (B- 2.7238 D)"
    },
    {
        "E(keV)": 1260.9,
        "Intensity": 5.4e-05,
        "Nuclide": "Sn-123 (B- 129.2 D)"
    },
    {
        "E(keV)": 1263.08,
        "Intensity": 0.0014,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 1264.98,
        "Intensity": 0.01648,
        "Nuclide": "Lu-174m (EC 142 D)"
    },
    {
        "E(keV)": 1269.6,
        "Intensity": 0.001845,
        "Nuclide": "As-74 (B- 17.77 D)"
    },
    {
        "E(keV)": 1271.88,
        "Intensity": 7.444,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 1273.52,
        "Intensity": 3.295,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 1274.436,
        "Intensity": 34.993,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 1274.53,
        "Intensity": 10.094,
        "Nuclide": "Na-22 (B+ 2.6088 Y)"
    },
    {
        "E(keV)": 1275.11,
        "Intensity": 0.119,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 1277.43,
        "Intensity": 2.886,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 1277.451,
        "Intensity": 1.68,
        "Nuclide": "Tm-168 (EC 93.1 D)"
    },
    {
        "E(keV)": 1280.25,
        "Intensity": 7.922,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 1283.28,
        "Intensity": 2.315,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 1288.76,
        "Intensity": 0.504,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 1290.585,
        "Intensity": 0.89,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 1291.596,
        "Intensity": 43.2,
        "Nuclide": "Fe-59 (B- 44.503 D)"
    },
    {
        "E(keV)": 1294.7,
        "Intensity": 2.842,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 1297.028,
        "Intensity": 5.15,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 1297.09,
        "Intensity": 71,
        "Nuclide": "Ca-47 (B- 4.536 D)"
    },
    {
        "E(keV)": 1297.91,
        "Intensity": 0.05438,
        "Nuclide": "Cs-132 (EC 6.479 D)"
    },
    {
        "E(keV)": 1299.14,
        "Intensity": 1.623,
        "Nuclide": "Eu-152 (B- 13.537 Y)"
    },
    {
        "E(keV)": 1312.096,
        "Intensity": 48.965,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 1312.12,
        "Intensity": 100.11,
        "Nuclide": "Sc-48 (B- 43.67 H)"
    },
    {
        "E(keV)": 1312.14,
        "Intensity": 2.863,
        "Nuclide": "Tb-160 (B- 72.3 D)"
    },
    {
        "E(keV)": 1317.473,
        "Intensity": 26.482,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 1317.927,
        "Intensity": 0.583,
        "Nuclide": "Cs-132 (EC 6.479 D)"
    },
    {
        "E(keV)": 1318.296,
        "Intensity": 0.03536,
        "Nuclide": "Lu-174 (EC 3.31 Y)"
    },
    {
        "E(keV)": 1323.6,
        "Intensity": 0.491,
        "Nuclide": "Rh-102m (EC 2.9 Y)"
    },
    {
        "E(keV)": 1325.5,
        "Intensity": 1.2,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 1325.508,
        "Intensity": 1.588,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 1331.997,
        "Intensity": 0.328,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 1332.21,
        "Intensity": 0.402,
        "Nuclide": "Kr-79 (EC 35.04 H)"
    },
    {
        "E(keV)": 1332.501,
        "Intensity": 99.986,
        "Nuclide": "Co-60 (B- 5.2714 Y)"
    },
    {
        "E(keV)": 1333.649,
        "Intensity": 3.576,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 1336.6,
        "Intensity": 3.443,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 1337.44,
        "Intensity": 0.000756,
        "Nuclide": "Sn-123 (B- 129.2 D)"
    },
    {
        "E(keV)": 1341.2,
        "Intensity": 3.155,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 1343.777,
        "Intensity": 2.66,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 1346.6,
        "Intensity": 0.0464,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 1349.89,
        "Intensity": 0.248,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 1355.175,
        "Intensity": 1.043,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 1360.215,
        "Intensity": 3.474,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 1361.0,
        "Intensity": 0.0004337,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 1362.1,
        "Intensity": 0.25,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 1362.9,
        "Intensity": 3.382,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 1364.6,
        "Intensity": 4.476,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 1365.185,
        "Intensity": 3.014,
        "Nuclide": "Cs-134 (B- 2.0648 Y)"
    },
    {
        "E(keV)": 1368.16,
        "Intensity": 2.623,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 1376.0,
        "Intensity": 1.345,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 1377.63,
        "Intensity": 46.067,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 1378.76,
        "Intensity": 0.00236,
        "Nuclide": "I-126 (EC 13.11 D)"
    },
    {
        "E(keV)": 1379.04,
        "Intensity": 2.315,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 1379.4,
        "Intensity": 0.93,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 1382.2,
        "Intensity": 0.0208,
        "Nuclide": "Y-88 (B+ 106.65 D)"
    },
    {
        "E(keV)": 1384.3,
        "Intensity": 24.121,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 1386.33,
        "Intensity": 0.102,
        "Nuclide": "Re-184 (EC 38.0 D)"
    },
    {
        "E(keV)": 1387.093,
        "Intensity": 5.58,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 1391.87,
        "Intensity": 2.282,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 1396.6,
        "Intensity": 0.0005956,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 1397.87,
        "Intensity": 0.786,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 1401.36,
        "Intensity": 0.003559,
        "Nuclide": "Te-129m (B- 33.6 D)"
    },
    {
        "E(keV)": 1405.15,
        "Intensity": 2.529,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 1407.64,
        "Intensity": 1.44,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 1408.006,
        "Intensity": 21.044,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 1418.243,
        "Intensity": 0.00184,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 1419.7,
        "Intensity": 0.487,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 1420.19,
        "Intensity": 0.292,
        "Nuclide": "I-126 (EC 13.11 D)"
    },
    {
        "E(keV)": 1421.67,
        "Intensity": 12.233,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 1423.19,
        "Intensity": 0.357,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 1427.3,
        "Intensity": 9.69,
        "Nuclide": "Re-182 (EC 64.0 H)"
    },
    {
        "E(keV)": 1428.08,
        "Intensity": 3.379,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 1434.092,
        "Intensity": 70.533,
        "Nuclide": "Mn-52 (EC 5.591 D)"
    },
    {
        "E(keV)": 1435.36,
        "Intensity": 6.415,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 1435.795,
        "Intensity": 66.575,
        "Nuclide": "La-138 (EC 1.05E+11 Y)"
    },
    {
        "E(keV)": 1436.561,
        "Intensity": 1.222,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 1437.35,
        "Intensity": 0.06027,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 1439.1,
        "Intensity": 0.279,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 1442.2,
        "Intensity": 0.13,
        "Nuclide": "Bi-207 (EC 31.55 Y)"
    },
    {
        "E(keV)": 1446.3,
        "Intensity": 0.0007807,
        "Nuclide": "Au-196 (EC 6.183 D)"
    },
    {
        "E(keV)": 1447.59,
        "Intensity": 0.00098,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 1448.776,
        "Intensity": 0.017,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 1449.106,
        "Intensity": 0.217,
        "Nuclide": "Eu-147 (EC 24 D)"
    },
    {
        "E(keV)": 1449.74,
        "Intensity": 10.906,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 1454.21,
        "Intensity": 0.05106,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 1457.643,
        "Intensity": 0.503,
        "Nuclide": "Eu-152 (EC 13.537 Y)"
    },
    {
        "E(keV)": 1460.83,
        "Intensity": 10.669,
        "Nuclide": "K-40 (EC 1.277E+9 Y)"
    },
    {
        "E(keV)": 1464.0,
        "Intensity": 0.134,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 1465.12,
        "Intensity": 22.2,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 1465.86,
        "Intensity": 4.5,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 1466.84,
        "Intensity": 3.652,
        "Nuclide": "Lu-169 (EC 34.06 H)"
    },
    {
        "E(keV)": 1468.89,
        "Intensity": 6.42,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 1470.28,
        "Intensity": 1.866,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 1474.88,
        "Intensity": 16.315,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 1475.788,
        "Intensity": 3.969,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 1475.9,
        "Intensity": 0.06128,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 1481.7,
        "Intensity": 0.059,
        "Nuclide": "Fe-59 (B- 44.503 D)"
    },
    {
        "E(keV)": 1485.49,
        "Intensity": 1.951,
        "Nuclide": "Eu-150 (EC 36.9 Y)"
    },
    {
        "E(keV)": 1486.099,
        "Intensity": 0.00056,
        "Nuclide": "Cd-115m (B- 44.6 D)"
    },
    {
        "E(keV)": 1488.888,
        "Intensity": 0.675,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 1494.048,
        "Intensity": 0.7,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 1505.04,
        "Intensity": 12.954,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 1508.1,
        "Intensity": 0.0006949,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 1509.49,
        "Intensity": 2.41,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 1510.6,
        "Intensity": 0.0004964,
        "Nuclide": "Pm-144 (EC 363 D)"
    },
    {
        "E(keV)": 1514.9,
        "Intensity": 3.989,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 1527.21,
        "Intensity": 11.261,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 1527.65,
        "Intensity": 16.557,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 1528.2,
        "Intensity": 0.0002,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 1529.64,
        "Intensity": 5.1,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 1531.8,
        "Intensity": 0.464,
        "Nuclide": "Rh-99 (B+ 16.1 D)"
    },
    {
        "E(keV)": 1532.14,
        "Intensity": 0.338,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 1533.711,
        "Intensity": 5.809,
        "Nuclide": "Eu-146 (EC 4.59 D)"
    },
    {
        "E(keV)": 1553.77,
        "Intensity": 83,
        "Nuclide": "V-50 (EC 1.4E+17 Y)"
    },
    {
        "E(keV)": 1558.31,
        "Intensity": 18.822,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 1561.8,
        "Intensity": 14.178,
        "Nuclide": "Ni-56 (EC 6.075 D)"
    },
    {
        "E(keV)": 1562.2,
        "Intensity": 0.07061,
        "Nuclide": "Rh-102 (EC 207 D)"
    },
    {
        "E(keV)": 1562.302,
        "Intensity": 1.022,
        "Nuclide": "Ag-110m (B- 249.79 D)"
    },
    {
        "E(keV)": 1562.51,
        "Intensity": 1.308,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 1570.68,
        "Intensity": 5.118,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 1572.35,
        "Intensity": 6.676,
        "Nuclide": "Ag-106m (EC 8.28 D)"
    },
    {
        "E(keV)": 1574.48,
        "Intensity": 2.77,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 1581.89,
        "Intensity": 0.187,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 1583.91,
        "Intensity": 0.576,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 1584.12,
        "Intensity": 2.702,
        "Nuclide": "Lu-172 (EC 6.70 D)"
    },
    {
        "E(keV)": 1590.4,
        "Intensity": 2.9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 1595.27,
        "Intensity": 5.102,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 1595.8,
        "Intensity": 1.712,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 1596.21,
        "Intensity": 95.4,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 1596.495,
        "Intensity": 1.788,
        "Nuclide": "Eu-154 (B- 8.593 Y)"
    },
    {
        "E(keV)": 1601.8,
        "Intensity": 9.149,
        "Nuclide": "Np-234 (EC 4.4 D)"
    },
    {
        "E(keV)": 1602.5,
        "Intensity": 0.003996,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 1604.5,
        "Intensity": 1.162,
        "Nuclide": "Tl-200 (EC 26.1 H)"
    },
    {
        "E(keV)": 1608.37,
        "Intensity": 4.14,
        "Nuclide": "Tm-172 (B- 63.6 H)"
    },
    {
        "E(keV)": 1614.3,
        "Intensity": 2.309,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 1620.2,
        "Intensity": 0.03767,
        "Nuclide": "Tc-95m (EC 61 D)"
    },
    {
        "E(keV)": 1620.8,
        "Intensity": 0.05662,
        "Nuclide": "Zr-89 (EC 78.41 H)"
    },
    {
        "E(keV)": 1621.51,
        "Intensity": 4.722,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 1646.24,
        "Intensity": 3.782,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 1650.37,
        "Intensity": 0.743,
        "Nuclide": "Br-82 (B- 35.30 H)"
    },
    {
        "E(keV)": 1650.436,
        "Intensity": 3.772,
        "Nuclide": "Eu-148 (EC 54.5 D)"
    },
    {
        "E(keV)": 1657.3,
        "Intensity": 0.08187,
        "Nuclide": "Zr-89 (EC 78.41 H)"
    },
    {
        "E(keV)": 1658.53,
        "Intensity": 14.748,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 1662.48,
        "Intensity": 0.12,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 1674.73,
        "Intensity": 0.441,
        "Nuclide": "Co-58 (EC 70.86 D)"
    },
    {
        "E(keV)": 1690.975,
        "Intensity": 47.794,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 1691.02,
        "Intensity": 8.371,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 1694.4,
        "Intensity": 0.0784,
        "Nuclide": "Cf-252,Cm-248 (SF)"
    },
    {
        "E(keV)": 1713.0,
        "Intensity": 0.575,
        "Nuclide": "Zr-89 (EC 78.41 H)"
    },
    {
        "E(keV)": 1715.67,
        "Intensity": 6.499,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 1718.7,
        "Intensity": 32.405,
        "Nuclide": "Bi-206 (EC 6.243 D)"
    },
    {
        "E(keV)": 1730.44,
        "Intensity": 0.02948,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 1734.12,
        "Intensity": 0.03863,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 1744.5,
        "Intensity": 0.09488,
        "Nuclide": "Zr-89 (EC 78.41 H)"
    },
    {
        "E(keV)": 1749.91,
        "Intensity": 0.0277,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 1752.4,
        "Intensity": 0.009188,
        "Nuclide": "Sb-122 (B- 2.7238 D)"
    },
    {
        "E(keV)": 1757.55,
        "Intensity": 3.243,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 1764.3,
        "Intensity": 32.936,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 1770.237,
        "Intensity": 6.871,
        "Nuclide": "Bi-207 (EC 31.55 Y)"
    },
    {
        "E(keV)": 1771.351,
        "Intensity": 12.528,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 1775.8,
        "Intensity": 4.044,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 1787.66,
        "Intensity": 0.293,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 1800.7,
        "Intensity": 9,
        "Nuclide": "Cf-252 (SF 2.645 Y)"
    },
    {
        "E(keV)": 1804.26,
        "Intensity": 1.059,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 1808.65,
        "Intensity": 18.206,
        "Nuclide": "Al-26 (EC 7.17E5 Y)"
    },
    {
        "E(keV)": 1830.49,
        "Intensity": 0.0085,
        "Nuclide": "Ho-166 (B- 26.80 H)"
    },
    {
        "E(keV)": 1836.063,
        "Intensity": 99.035,
        "Nuclide": "Y-88 (B+ 106.65 D)"
    },
    {
        "E(keV)": 1845.45,
        "Intensity": 4.12,
        "Nuclide": "Tb-156 (EC 5.35 D)"
    },
    {
        "E(keV)": 1847.5,
        "Intensity": 0.852,
        "Nuclide": "Nb-92m (EC 10.15 D)"
    },
    {
        "E(keV)": 1857.66,
        "Intensity": 0.39,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 1861.7,
        "Intensity": 6.259,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 1876.67,
        "Intensity": 1.319,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 1878.0,
        "Intensity": 0.02698,
        "Nuclide": "Ca-47 (B- 4.536 D)"
    },
    {
        "E(keV)": 1885.9,
        "Intensity": 1.895,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 1887.0,
        "Intensity": 1.406,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 1891.48,
        "Intensity": 0.366,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 1897.42,
        "Intensity": 0.01566,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 1897.751,
        "Intensity": 0.541,
        "Nuclide": "Rb-84 (EC 32.77 D)"
    },
    {
        "E(keV)": 1903.45,
        "Intensity": 2.502,
        "Nuclide": "Bi-205 (EC 15.31 D)"
    },
    {
        "E(keV)": 1919.52,
        "Intensity": 6.91,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 1924.18,
        "Intensity": 2.018,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 1944.08,
        "Intensity": 4.131,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 1952.06,
        "Intensity": 0.574,
        "Nuclide": "Sr-83 (B+ 32.41 H)"
    },
    {
        "E(keV)": 1965.95,
        "Intensity": 3.87,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 1985.638,
        "Intensity": 0.06992,
        "Nuclide": "Cs-132 (EC 6.479 D)"
    },
    {
        "E(keV)": 1991.15,
        "Intensity": 0.04233,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 1997.0,
        "Intensity": 7.082,
        "Nuclide": "Eu-145 (EC 5.93 D)"
    },
    {
        "E(keV)": 2002.134,
        "Intensity": 1.921,
        "Nuclide": "Sn-125 (B- 9.64 D)"
    },
    {
        "E(keV)": 2010.0,
        "Intensity": 1.3e-05,
        "Nuclide": "Sc-46 (B- 83.810 D)"
    },
    {
        "E(keV)": 2015.181,
        "Intensity": 2.462,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 2023.65,
        "Intensity": 0.413,
        "Nuclide": "Ge-69 (EC 39.05 H)"
    },
    {
        "E(keV)": 2026.65,
        "Intensity": 3.272,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 2034.755,
        "Intensity": 6.389,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 2038.3,
        "Intensity": 0.271,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 2040.0,
        "Intensity": 2.542,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 2041.88,
        "Intensity": 5.908,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 2043.67,
        "Intensity": 3.607,
        "Nuclide": "Au-194 (EC 38.02 H)"
    },
    {
        "E(keV)": 2045.09,
        "Intensity": 0.004589,
        "Nuclide": "I-126 (EC 13.11 D)"
    },
    {
        "E(keV)": 2049.78,
        "Intensity": 5.245,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 2059.65,
        "Intensity": 7.427,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 2078.86,
        "Intensity": 0.276,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 2089.57,
        "Intensity": 4.626,
        "Nuclide": "Te-119m (EC 4.70 D)"
    },
    {
        "E(keV)": 2090.936,
        "Intensity": 5.512,
        "Nuclide": "Sb-124 (B- 60.20 D)"
    },
    {
        "E(keV)": 2091.0,
        "Intensity": 0.455,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 2096.3,
        "Intensity": 0.549,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 2096.9,
        "Intensity": 6.034,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 2097.7,
        "Intensity": 3.809,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 2099.1,
        "Intensity": 4.951,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 2105.9,
        "Intensity": 0.07696,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 2110.8,
        "Intensity": 0.329,
        "Nuclide": "As-76 (B- 1.0778 D)"
    },
    {
        "E(keV)": 2126.11,
        "Intensity": 4.968,
        "Nuclide": "Lu-170 (EC 2.012 D)"
    },
    {
        "E(keV)": 2133.04,
        "Intensity": 0.01612,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 2158.77,
        "Intensity": 0.00111,
        "Nuclide": "Co-60 (B- 5.2714 Y)"
    },
    {
        "E(keV)": 2186.242,
        "Intensity": 1.4e-06,
        "Nuclide": "Y-90 (B- 64.10 H)"
    },
    {
        "E(keV)": 2186.71,
        "Intensity": 3.485,
        "Nuclide": "Eu-156 (B- 15.19 D)"
    },
    {
        "E(keV)": 2193.67,
        "Intensity": 2.12,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 2198.2,
        "Intensity": 0.008324,
        "Nuclide": "As-74 (EC 17.77 D)"
    },
    {
        "E(keV)": 2201.72,
        "Intensity": 0.05859,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 2214.59,
        "Intensity": 19.65,
        "Nuclide": "Ir-188 (EC 41.5 H)"
    },
    {
        "E(keV)": 2232.25,
        "Intensity": 0.455,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 2240.395,
        "Intensity": 1.21,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 2248.5,
        "Intensity": 0.03819,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 2283.25,
        "Intensity": 0.527,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 2284.39,
        "Intensity": 0.0444,
        "Nuclide": "Pm-148 (B- 5.370 D)"
    },
    {
        "E(keV)": 2347.88,
        "Intensity": 0.849,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 2375.1,
        "Intensity": 0.005022,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 2421.8,
        "Intensity": 0.005022,
        "Nuclide": "V-48 (EC 15.9735 D)"
    },
    {
        "E(keV)": 2505.0,
        "Intensity": 2e-06,
        "Nuclide": "Co-60 (B- 5.2714 Y)"
    },
    {
        "E(keV)": 2507.86,
        "Intensity": 0.03906,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 2521.4,
        "Intensity": 3.463,
        "Nuclide": "La-140 (B- 1.6781 D)"
    },
    {
        "E(keV)": 2598.459,
        "Intensity": 14.01,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 2610.0,
        "Intensity": 100,
        "Nuclide": "Bi-208 (EC 3.68E+5 Y)"
    },
    {
        "E(keV)": 2621.46,
        "Intensity": 0.04676,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 2730.91,
        "Intensity": 0.01119,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 2734.0,
        "Intensity": 0.713,
        "Nuclide": "Y-88 (B+ 106.65 D)"
    },
    {
        "E(keV)": 2746.9,
        "Intensity": 0.368,
        "Nuclide": "I-124 (EC 4.1760 D)"
    },
    {
        "E(keV)": 2804.2,
        "Intensity": 0.05528,
        "Nuclide": "Ni-57 (B+ 35.60 H)"
    },
    {
        "E(keV)": 2938.0,
        "Intensity": 0.0438,
        "Nuclide": "Al-26 (EC 7.17E5 Y)"
    },
    {
        "E(keV)": 2940.07,
        "Intensity": 0.03598,
        "Nuclide": "As-72 (EC 26.0 H)"
    },
    {
        "E(keV)": 3009.596,
        "Intensity": 0.939,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 3201.962,
        "Intensity": 2.689,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 3219.7,
        "Intensity": 0.007031,
        "Nuclide": "Y-88 (B+ 106.65 D)"
    },
    {
        "E(keV)": 3253.416,
        "Intensity": 6.576,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 3272.99,
        "Intensity": 1.563,
        "Nuclide": "Co-56 (EC 77.233 D)"
    },
    {
        "E(keV)": 3451.152,
        "Intensity": 0.787,
        "Nuclide": "Co-56 (EC 77.233 D)"
    }
]

class SearchConstructor:
    def __init__(self):
        return
    def InRange(self, Energy: float, LeftRightRange: float) -> List[ReturnItem]:
        """
        Docstring for InRange
        
        :param self: Returns a ordered list of Nuclides, using the users inputs as for search recomendations. This library was downloaded from atom.kaeri.re.kr
        :param Energy: In keV, this value is used to search the closest Nuclides to that energy.
        :type Energy: float
        :param LeftRightRange: In keV, is the sort of distance from the energy input that requires searched Nuclides to stay within.
        :type LeftRightRange: float
        :return: Returns a ordered list of Nuclides
        :rtype: List[ReturnItem]
        """
        ReturnList: List[ReturnItem] = []
        LeftVal: float = (Energy - (LeftRightRange/2))
        RightVal: float = (Energy + (LeftRightRange/2))
        for i in GlobalLibrary:
            if i["E(keV)"] >= LeftVal and i["E(keV)"] <= RightVal:
                Item = ReturnItem(i['Nuclide'], i['Intensity'], i["E(keV)"])
                ReturnList.append(Item)
        return ReturnList



class CreateSearch:
    def __init__(self):
        self.Search = SearchConstructor()
        return