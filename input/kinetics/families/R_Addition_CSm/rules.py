#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_CSm/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 416,
    label = "CSm;Y_rad",
    group1 = 
"""
1 *1 C u2 {2,D}
2    S u0 {1,D}
""",
    group2 = 
"""
1 *2 R u1
""",
    kinetics = ArrheniusEP(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
)

entry(
    index = 417,
    label = "CSm;H_rad",
    group1 = 
"""
1 *1 C u2 {2,D}
2    S u0 {1,D}
""",
    group2 = 
"""
1 *2 H u1
""",
    kinetics = ArrheniusEP(
        A = (1.18e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Guessed from CO+H_rad""",
    longDesc = 
u"""

""",
)

entry(
    index = 418,
    label = "CSm;C_methyl",
    group1 = 
"""
1 *1 C u2 {2,D}
2    S u0 {1,D}
""",
    group2 = 
"""
1 *2 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 2.11,
        alpha = 0,
        E0 = (2.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CAC CBS-QB3 calc (using methyl group), HO Approx""",
    longDesc = 
u"""

""",
)

entry(
    index = 419,
    label = "CSm;CH2CH3",
    group1 = 
"""
1 *1 C u2 {2,D}
2    S u0 {1,D}
""",
    group2 = 
"""
1 *2 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S} {5,S} {6,S} {7,S}
5    H  u0 {4,S}
6    H  u0 {4,S}
7    H  u0 {4,S}
""",
    kinetics = ArrheniusEP(
        A = (2.01e+10, 'cm^3/(mol*s)'),
        n = 2.22,
        alpha = 0,
        E0 = (0.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CAC CBS-QB3 calc (using ethyl group), HO approx""",
    longDesc = 
u"""

""",
)

