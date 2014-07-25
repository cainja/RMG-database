#!/usr/bin/env python
# encoding: utf-8

name = "combustion_core/version5"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    reactant1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+06, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 2.1,
        Ea = (6.57, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    reactant1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.06e+06, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 2.1,
        Ea = (6.57, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product1 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (196.9, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product3 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product3 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.15e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.48e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product3 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.13e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.12e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (7.09, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product3 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+12, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (3.58, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    reactant1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+07, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 1.3,
        Ea = (-3.2, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    reactant1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+14, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (99.02, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    reactant1 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    reactant2 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+10, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    reactant1 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (14.13, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    reactant1 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+12, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    reactant1 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    reactant1 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    reactant1 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    reactant1 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    reactant1 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 O u0 p2 c0  {1,S} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.68e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    reactant1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    reactant1 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u1 p0 c0  {1,T}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u1 p0 c0  {1,D} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    reactant1 = 
"""
H2CCCH
multiplicity 2
1 C u1 p0 c0  {2,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {3,T}
3 C u0 p0 c0  {2,T} {6,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {3,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product3 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    reactant1 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    reactant1 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+14, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    reactant1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    reactant1 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    reactant1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product3 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    reactant1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    reactant1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    reactant1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u1 p0 c0  {1,D} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    reactant1 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    reactant1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (3.33, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    reactant1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product3 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+14, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (3.33, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    reactant1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+13, 'cm^3/(mol*s)', '*|/', 1.4),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    reactant1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
C2H3
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u1 p0 c0  {1,D} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    reactant1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    reactant1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u1 p0 c0  {1,T}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (8.37, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    reactant1 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (42, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    reactant1 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    reactant1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C3H4
1 C u0 p0 c0  {2,D} {4,S} {5,S}
2 C u0 p0 c0  {1,D} {3,D}
3 C u0 p0 c0  {2,D} {6,S} {7,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {3,S}
7 H u0 p0 c0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (27.69, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    reactant1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2CCCH
multiplicity 2
1 C u1 p0 c0  {2,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {3,T}
3 C u0 p0 c0  {2,T} {6,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {3,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+14, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    reactant1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    reactant1 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C3H6
1 C u0 p0 c0  {2,D} {4,S} {5,S}
2 C u0 p0 c0  {1,D} {3,S} {6,S}
3 C u0 p0 c0  {2,S} {7,S} {8,S} {9,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {3,S}
8 H u0 p0 c0  {3,S}
9 H u0 p0 c0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    reactant1 = 
"""
C2H6
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
C2H5
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    reactant1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
H2CCCCH
multiplicity 2
1 C u0 p0 c0  {2,D} {5,S} {6,S}
2 C u1 p0 c0  {1,D} {3,S}
3 C u0 p0 c0  {2,S} {4,T}
4 C u0 p0 c0  {3,T} {7,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 H u0 p0 c0  {4,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+09, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (242, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    reactant1 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH2HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {3,D} {6,S}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.74e+06, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 1.88,
        Ea = (0.75, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    reactant1 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.13e+06, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 1.88,
        Ea = (0.75, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    reactant1 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (680000, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 1.88,
        Ea = (0.75, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    reactant1 = 
"""
C4H2
1 C u0 p0 c0  {2,S} {3,T}
2 C u0 p0 c0  {1,S} {4,T}
3 C u0 p0 c0  {1,T} {5,S}
4 C u0 p0 c0  {2,T} {6,S}
5 H u0 p0 c0  {3,S}
6 H u0 p0 c0  {4,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C3H2
multiplicity 1
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {3,S} {5,S}
3 C u2 p0 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.68e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (-1.71, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant3 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.89e+15, 'cm^6/(mol^2*s)', '*|/', 1.5),
        n = 0,
        Ea = (-8.73, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+11, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (37.42, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u1 p0 c0  {1,T}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
C3H2
multiplicity 1
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {3,S} {5,S}
3 C u2 p0 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
H2CCCH
multiplicity 2
1 C u1 p0 c0  {2,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {3,T}
3 C u0 p0 c0  {2,T} {6,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {3,S}
""",
    product1 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+10, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (12, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    reactant1 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (16.59, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    reactant1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 1.6),
        n = 0,
        Ea = (56.54, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+14, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (3.66, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (7.2, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH2OH
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 O u0 p2 c0  {1,S} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    reactant1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+13, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    reactant1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    reactant1 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u1 p0 c0  {1,T}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HCCO
multiplicity 2
1 C u1 p0 c0  {2,D} {4,S}
2 C u0 p0 c0  {1,D} {3,D}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.62e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (131.37, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+09, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 1.14,
        Ea = (0.42, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    reactant1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (51200, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 2.67,
        Ea = (26.27, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    reactant1 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.52e+08, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 1.6,
        Ea = (77.08, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    reactant1 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+08, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 1.56,
        Ea = (35.5, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    reactant1 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.57e+07, 'cm^3/(mol*s)', '*|/', 1.15),
        n = 1.83,
        Ea = (11.64, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    reactant1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u1 p0 c0  {1,T}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (54.04, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    reactant1 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u1 p0 c0  {1,D} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.42e+14, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (62.36, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    reactant1 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u1 p0 c0  {1,D} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (24.86, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    reactant1 = 
"""
C2H6
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+09, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 1.5,
        Ea = (31.01, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    reactant1 = 
"""
C2H6
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e-07, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 6,
        Ea = (25.3, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    reactant1 = 
"""
C2H6
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+09, 'cm^3/(mol*s)', '*|/', 1.15),
        n = 1.5,
        Ea = (24.28, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    reactant1 = 
"""
C2H6
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+06, 'cm^3/(mol*s)', '*|/', 1.1),
        n = 2,
        Ea = (3.62, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    reactant1 = 
"""
C2H6
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
C2H5
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (85.63, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (170.11, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+10, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (7.32, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    reactant1 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+12, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (15.71, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    reactant1 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.62e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (16.63, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    reactant1 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.83e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (5.57, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    reactant1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+08, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 1.62,
        Ea = (9.06, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    reactant1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.09e+12, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        Ea = (36.95, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    reactant1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.16e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0.57,
        Ea = (11.56, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    reactant1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 1.18,
        Ea = (-1.87, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (5.9, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    reactant1 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.19e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (-2.08, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    reactant1 = 
"""
C4H10
1  C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0  {1,S}
6  H u0 p0 c0  {1,S}
7  H u0 p0 c0  {2,S}
8  H u0 p0 c0  {2,S}
9  H u0 p0 c0  {3,S}
10 H u0 p0 c0  {3,S}
11 H u0 p0 c0  {3,S}
12 H u0 p0 c0  {4,S}
13 H u0 p0 c0  {4,S}
14 H u0 p0 c0  {4,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C4H9_1
multiplicity 2
1  C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0  {2,S} {12,S} {13,S}
5  H u0 p0 c0  {1,S}
6  H u0 p0 c0  {1,S}
7  H u0 p0 c0  {2,S}
8  H u0 p0 c0  {2,S}
9  H u0 p0 c0  {3,S}
10 H u0 p0 c0  {3,S}
11 H u0 p0 c0  {3,S}
12 H u0 p0 c0  {4,S}
13 H u0 p0 c0  {4,S}
""",
    product2 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (81.1, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    reactant1 = 
"""
C4H10
1  C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0  {1,S}
6  H u0 p0 c0  {1,S}
7  H u0 p0 c0  {2,S}
8  H u0 p0 c0  {2,S}
9  H u0 p0 c0  {3,S}
10 H u0 p0 c0  {3,S}
11 H u0 p0 c0  {3,S}
12 H u0 p0 c0  {4,S}
13 H u0 p0 c0  {4,S}
14 H u0 p0 c0  {4,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C4H9_2
multiplicity 2
1  C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0  {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0  {1,S} {3,S} {13,S}
5  H u0 p0 c0  {1,S}
6  H u0 p0 c0  {1,S}
7  H u0 p0 c0  {2,S}
8  H u0 p0 c0  {2,S}
9  H u0 p0 c0  {2,S}
10 H u0 p0 c0  {3,S}
11 H u0 p0 c0  {3,S}
12 H u0 p0 c0  {3,S}
13 H u0 p0 c0  {4,S}
""",
    product2 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.76e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (71.1, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    reactant1 = 
"""
C4H10
1  C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0  {1,S}
6  H u0 p0 c0  {1,S}
7  H u0 p0 c0  {2,S}
8  H u0 p0 c0  {2,S}
9  H u0 p0 c0  {3,S}
10 H u0 p0 c0  {3,S}
11 H u0 p0 c0  {3,S}
12 H u0 p0 c0  {4,S}
13 H u0 p0 c0  {4,S}
14 H u0 p0 c0  {4,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C4H9_1
multiplicity 2
1  C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0  {2,S} {12,S} {13,S}
5  H u0 p0 c0  {1,S}
6  H u0 p0 c0  {1,S}
7  H u0 p0 c0  {2,S}
8  H u0 p0 c0  {2,S}
9  H u0 p0 c0  {3,S}
10 H u0 p0 c0  {3,S}
11 H u0 p0 c0  {3,S}
12 H u0 p0 c0  {4,S}
13 H u0 p0 c0  {4,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+07, 'cm^3/(mol*s)', '*|/', 2),
        n = 1.8,
        Ea = (3.99, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    reactant1 = 
"""
C4H10
1  C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0  {1,S}
6  H u0 p0 c0  {1,S}
7  H u0 p0 c0  {2,S}
8  H u0 p0 c0  {2,S}
9  H u0 p0 c0  {3,S}
10 H u0 p0 c0  {3,S}
11 H u0 p0 c0  {3,S}
12 H u0 p0 c0  {4,S}
13 H u0 p0 c0  {4,S}
14 H u0 p0 c0  {4,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C4H9_2
multiplicity 2
1  C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0  {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0  {1,S} {3,S} {13,S}
5  H u0 p0 c0  {1,S}
6  H u0 p0 c0  {1,S}
7  H u0 p0 c0  {2,S}
8  H u0 p0 c0  {2,S}
9  H u0 p0 c0  {2,S}
10 H u0 p0 c0  {3,S}
11 H u0 p0 c0  {3,S}
12 H u0 p0 c0  {3,S}
13 H u0 p0 c0  {4,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.36e+06, 'cm^3/(mol*s)', '*|/', 2),
        n = 2,
        Ea = (-2.49, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    reactant1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (4.18, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
C2H3
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u1 p0 c0  {1,D} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+16, 'cm^3/(mol*s)', '*|/', 3.16),
        n = -1.39,
        Ea = (4.22, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    reactant1 = 
"""
C4H2
1 C u0 p0 c0  {2,S} {3,T}
2 C u0 p0 c0  {1,S} {4,T}
3 C u0 p0 c0  {1,T} {5,S}
4 C u0 p0 c0  {2,T} {6,S}
5 H u0 p0 c0  {3,S}
6 H u0 p0 c0  {4,S}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
C3H2
multiplicity 1
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {3,S} {5,S}
3 C u2 p0 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (7.19648, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    reactant1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u1 p0 c0  {1,T}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C4H2
1 C u0 p0 c0  {2,S} {3,T}
2 C u0 p0 c0  {1,S} {4,T}
3 C u0 p0 c0  {1,T} {5,S}
4 C u0 p0 c0  {2,T} {6,S}
5 H u0 p0 c0  {3,S}
6 H u0 p0 c0  {4,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.37156e+29, 'cm^3/(mol*s)', '*|/', 1.5),
        n = -6.78459,
        Ea = (17.5993, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+14, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (63.9566, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    reactant1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.54e+15, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = 0,
            Ea = (12.56, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    reactant1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.4e+36, 'cm^3/(mol*s)', '*|/', 1.2),
            n = -5.54,
            Ea = (404.58, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    reactant1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.26e+36, 'cm^3/(mol*s)', '*|/', 1.2),
            n = -5.54,
            Ea = (404.58, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    reactant1 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    product1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.57e+15, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (241.03, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    reactant1 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.51e+13, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 0.48, 'O=C=O': 1.5, 'CC': 1.44, 'O': 6.5, '[O][O]': 0.4, '[C]=O': 0.75, 'N#N': 0.4, 'C=C': 1.6, 'C#C': 3.2, '[Ar]': 0.24},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    reactant1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.91e+16, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (379.14, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    reactant1 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (9.97e+16, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (299.32, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    reactant1 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.4e+13, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = 0,
            Ea = (-7.48, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.1e+18, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = -0.8,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 0, '[O][O]': 0.4, 'N#N': 0.67, '[C]=O': 0.75, '[Ar]': 0.29},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    reactant1 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u1 p0 c0  {1,D} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (7.4e+17, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (404.09, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.87e+18, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = -1,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[H][H]': 0, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
O
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.18e+19, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = -1,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.53e+22, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = -2,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 2.55, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.15},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.55e+14, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (56.46, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 O u0 p2 c0  {1,S} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.26e+16, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (125.6, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    reactant1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u1 p0 c0  {1,D} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.43e+12, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (10.81, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(3.43e+18, 'cm^6/(mol^2*s)'), n=0, Ea=(6.15, 'kJ/mol'), T0=(1, 'K')),
        alpha = 1,
        T3 = (1, 'K'),
        T1 = (1, 'K'),
        T2 = (1231, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    reactant1 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (3.97e+09, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 1.28,
            Ea = (5.4, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(1.35e+19, 'cm^6/(mol^2*s)'), n=0, Ea=(3.16, 'kJ/mol'), T0=(1, 'K')),
        alpha = 0.76,
        T3 = (40, 'K'),
        T1 = (1025, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (7.23e+13, 'cm^3/(mol*s)', '*|/', 1.2),
            n = -0.37,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.53e+19, 'cm^6/(mol^2*s)'),
            n = -0.76,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1, 'K'),
        T1 = (1, 'K'),
        T2 = (1040, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.688e+14, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.408e+24, 'cm^6/(mol^2*s)'),
            n = -1.8,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.37,
        T3 = (3315, 'K'),
        T1 = (61, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    reactant1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H6
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (3.61e+13, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.63e+41, 'cm^6/(mol^2*s)'),
            n = -7,
            Ea = (11.56, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.62,
        T3 = (73, 'K'),
        T1 = (1180, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    reactant1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.87e+17, 'cm^3/(mol*s)'),
            n = -1,
            Ea = (71.128, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 0, '[H][H]': 2, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    reactant1 = 
"""
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.4209, -0.799241, -0.299133, -0.0143012],
            [0.236291, 0.856853, 0.246313, -0.0463755],
            [-0.0827561, 0.0457236, 0.105699, 0.057531],
            [-0.049145, -0.0760609, -0.0214574, 0.0247001],
            [-0.00664556, -0.0412733, -0.0308561, -0.00959838],
            [0.0111919, -0.00649914, -0.0106088, -0.0137528],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.0013156, 'atm'),
        Pmax = (131.56, 'atm'),
        comment = 'Reaction and kinetics from combustion_core/version5.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

