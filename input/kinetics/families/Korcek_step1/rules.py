#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step1/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "RCH(OOH)CH2C(O)R'",
    group1 = 
"""
1     C u0 {2,S} {4,S} {7,S} {9,S}
2     C u0 {1,S} {3,S} {11,S} {12,S}
3  *4 C u0 {2,S} {6,D} {8,S}
4     O u0 {1,S} {5,S}
5  *1 O u0 {4,S} {10,S}
6  *3 O u0 {3,D}
7     R u0 {1,S}
8     R u0 {3,S}
9     H u0 {1,S}
10 *2 H u0 {5,S}
11    H u0 {2,S}
12    H u0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2.1e-12, 's^-1'),
        n = 6.17,
        alpha = 0,
        E0 = (19.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""CanTherm calculations using F12-QZ energies for reactants and TS. b3lyp/cbsb7 rotor potentials for HOOQ=O were used.""",
    longDesc = 
u"""

""",
)

