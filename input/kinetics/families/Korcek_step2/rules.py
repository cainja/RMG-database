#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step2/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C1(R)(H)(O[OC3(OH)(R')]C2)",
    group1 = 
"""
1  *1 C u0 {2,S} {4,S} {7,S} {9,S}
2  *2 C u0 {1,S} {3,S} {11,S} {12,S}
3  *3 C u0 {2,S} {5,S} {6,S} {8,S}
4  *5 O u0 {1,S} {5,S}
5  *4 O u0 {3,S} {4,S}
6     O u0 {3,S} {10,S}
7     R u0 {1,S}
8     R u0 {3,S}
9  *6 H u0 {1,S}
10    H u0 {6,S}
11    H u0 {2,S}
12    H u0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3e+09, 's^-1'),
        n = 1.38,
        alpha = 0,
        E0 = (34.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""CanTherm calculations using F12-QZ energies for reactants and TS. OH rotor potentials for cyclic peroxide obtained at th3 b3lyp/cbsb7 level of theory""",
    longDesc = 
u"""

""",
)

