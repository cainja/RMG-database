#!/usr/bin/env python
# encoding: utf-8

name = "GRI-Mech3.0-N"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    reactant1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
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
        A = (38700, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (6260, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
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
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.63e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (4000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
    kinetics = Arrhenius(
        A = (5.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
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
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.06e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
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
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
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
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
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
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
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
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3540, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
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
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
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
CH2OH
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 O u0 p2 c0  {1,S} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (388000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (3100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
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
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 C u1 p0 c0  {1,T}
""",
    product1 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 C u1 p0 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+19, 'cm^3/(mol*s)'),
        n = -1.41,
        Ea = (28950, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
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
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.94e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
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
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e+07, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (220, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
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
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.24e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
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
    product1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
        A = (8.98e+07, 'cm^3/(mol*s)'),
        n = 1.92,
        Ea = (5690, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
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
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
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
CH2(T)
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
        A = (1.75e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1350, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O
multiplicity 3
1 O u2 p2 c0 
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
        A = (2.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant3 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
        A = (2.08e+19, 'cm^6/(mol^2*s)'),
        n = -1.24,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
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
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
        A = (1.126e+19, 'cm^6/(mol^2*s)'),
        n = -0.76,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant3 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+19, 'cm^6/(mol^2*s)'),
        n = -1.24,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
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
        A = (2.65e+16, 'cm^3/(mol*s)'),
        n = -0.6707,
        Ea = (17041, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
    reactant3 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+16, 'cm^6/(mol^2*s)'),
        n = -0.6,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
    reactant3 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+19, 'cm^6/(mol^2*s)'),
        n = -1.25,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
    reactant3 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
        A = (5.5e+20, 'cm^6/(mol^2*s)'),
        n = -2,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
O(T)
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
        A = (3.97e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (671, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.48e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1068, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
        A = (8.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (635, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (5200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
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
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C(T)
multiplicity 3
1 C u4 p0 c0 
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
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
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (10840, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
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
    kinetics = Arrhenius(
        A = (7.34e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
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
        A = (5.74e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2742, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.65,
        Ea = (-284, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
    kinetics = Arrhenius(
        A = (3.28e+13, 'cm^3/(mol*s)'),
        n = -0.09,
        Ea = (610, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH2OH
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 O u0 p2 c0  {1,S} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.15e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (1924, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
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
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-110, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
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
    kinetics = Arrhenius(
        A = (2.62e+14, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (1070, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
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
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+07, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4870, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+06, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4870, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
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
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
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
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.325e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12240, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
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
    product1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
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
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
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
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
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
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
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
        A = (1.13e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3428, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HCCOH
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 O u0 p2 c0  {1,S} {5,S}
4 H u0 p0 c0  {2,S}
5 H u0 p0 c0  {3,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
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
        A = (2.16e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O(T)
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
        A = (35700, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (-2110, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.45e+13, 'cm^3/(mol*s)'), n=0, Ea=(-500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5e+15, 'cm^3/(mol*s)'), n=0, Ea=(17330, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(427, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.7e+18, 'cm^3/(mol*s)'), n=0, Ea=(29410, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
C(T)
multiplicity 3
1 C u4 p0 c0 
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
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
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
        A = (1.13e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
CH2(T)
multiplicity 3
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
    kinetics = Arrhenius(
        A = (5.6e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (5420, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
    kinetics = Arrhenius(
        A = (6.44e+17, 'cm^3/(mol*s)'),
        n = -1.34,
        Ea = (1417, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
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
        A = (1e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (3120, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
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
        A = (4.76e+07, 'cm^3/(mol*s)'),
        n = 1.228,
        Ea = (70, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
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
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
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
        A = (3.43e+09, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-447, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
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
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
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
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.44e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-840, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
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
        A = (6.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 C u1 p0 c0  {1,T}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000218, 'cm^3/(mol*s)'),
        n = 4.5,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HCCOH
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 O u0 p2 c0  {1,S} {5,S}
4 H u0 p0 c0  {2,S}
5 H u0 p0 c0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (504000, 'cm^3/(mol*s)'),
        n = 2.3,
        Ea = (13500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
C2H
multiplicity 2
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 C u1 p0 c0  {1,T}
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
        A = (3.37e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (14000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
        A = (0.000483, 'cm^3/(mol*s)'),
        n = 4,
        Ea = (-2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
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
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
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
        A = (3.54e+06, 'cm^3/(mol*s)'),
        n = 2.12,
        Ea = (870, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
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
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
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
        A = (7.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1630, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
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
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.78e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
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
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (23600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
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
        A = (5.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (12000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
C(T)
multiplicity 3
1 C u4 p0 c0 
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (576, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
C(T)
multiplicity 3
1 C u4 p0 c0 
""",
    reactant2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
C2H
multiplicity 2
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 C u1 p0 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
C(T)
multiplicity 3
1 C u4 p0 c0 
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.71e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3110, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.71e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-755, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
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
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15792, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.46e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-515, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
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
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
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
        A = (500000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (7230, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11944, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(T)
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
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
        A = (2.46e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8270, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
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
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product1 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
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
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
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
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2
1 H u0 p0 c0  {2,S}
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH2(T)
multiplicity 3
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
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-570, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
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
        A = (1.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-570, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product1 = 
"""
CH2(T)
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
        A = (9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
CH2(T)
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
        A = (7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
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
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-550, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
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
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product2 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.56e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
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
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
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
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20315, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
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
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
        A = (24500, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (5180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
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
H
multiplicity 2
1 H u1 p0 c0 
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
        A = (6.84e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
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
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
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
        A = (2.648e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
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
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
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
        A = (3320, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (5860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
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
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
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
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9940, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
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
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
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
        A = (1e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9940, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
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
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (227000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (9200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
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
        A = (6.14e+06, 'cm^3/(mol*s)'),
        n = 1.74,
        Ea = (10450, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    reactant1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    reactant2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
    product3 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+18, 'cm^3/(mol*s)'),
        n = -1,
        Ea = (17000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    reactant1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.345e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
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
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3530, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    reactant1 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 C u1 p0 c0  {1,T}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-755, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    reactant1 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 C u1 p0 c0  {1,T}
""",
    reactant2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.68e+10, 'cm^3/(mol*s)'),
        n = 0.9,
        Ea = (1993, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
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
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1015, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
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
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3875, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    reactant1 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
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
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (854, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    reactant1 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
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
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    reactant1 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (355, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    reactant1 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (6500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    reactant1 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
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
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.36e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (385, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    reactant1 = 
"""
N2O
1 N u0 p0 c+1 {2,D} {3,D}
2 N u0 p2 c-1 {1,D}
3 O u0 p2 c0  {1,D}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
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
        A = (1.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10810, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    reactant1 = 
"""
N2O
1 N u0 p0 c+1 {2,D} {3,D}
2 N u0 p2 c-1 {1,D}
3 O u0 p2 c0  {1,D}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (23150, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    reactant1 = 
"""
N2O
1 N u0 p0 c+1 {2,D} {3,D}
2 N u0 p2 c-1 {1,D}
3 O u0 p2 c0  {1,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
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
        A = (3.87e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18880, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    reactant1 = 
"""
N2O
1 N u0 p0 c+1 {2,D} {3,D}
2 N u0 p2 c-1 {1,D}
3 O u0 p2 c0  {1,D}
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
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (21060, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    reactant1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
NO2
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 O u1 p2 c0  {1,S}
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
        A = (2.11e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    reactant1 = 
"""
NO2
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
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
        A = (3.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-240, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    reactant1 = 
"""
NO2
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
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
        A = (1.32e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (360, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (330, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
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
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
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
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
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
N
multiplicity 4
1 N u3 p1 c0 
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
        A = (2e+09, 'cm^3/(mol*s)'),
        n = 1.2,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (461000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (6500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
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
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
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
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13850, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
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
        A = (2.16e+13, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
N2O
1 N u0 p0 c+1 {2,D} {3,D}
2 N u0 p2 c-1 {1,D}
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
        A = (3.65e+14, 'cm^3/(mol*s)'),
        n = -0.45,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    reactant1 = 
"""
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O(T)
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
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    reactant1 = 
"""
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O(T)
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
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    reactant1 = 
"""
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
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
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3650, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    reactant1 = 
"""
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
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
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
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
        A = (9e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-460, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    reactant1 = 
"""
NNH
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 N u1 p1 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (3.3e+08, 's^-1'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    reactant1 = 
"""
NNH
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 N u1 p1 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    reactant1 = 
"""
NNH
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 N u1 p1 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O(T)
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
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    reactant1 = 
"""
NNH
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 N u1 p1 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    reactant1 = 
"""
NNH
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 N u1 p1 c0  {1,D}
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
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    reactant1 = 
"""
NNH
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 N u1 p1 c0  {1,D}
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
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    reactant1 = 
"""
NNH
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 N u1 p1 c0  {1,D}
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
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    reactant1 = 
"""
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
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
        A = (2.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    reactant1 = 
"""
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
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
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+11, 'cm^3/(mol*s)'),
        n = 0.72,
        Ea = (660, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    reactant1 = 
"""
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
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
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
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
        A = (1.3e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (-950, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    reactant1 = 
"""
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    reactant1 = 
"""
CN
multiplicity 2
1 C u1 p0 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    reactant2 = 
"""
O(T)
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
N
multiplicity 4
1 N u3 p1 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    reactant1 = 
"""
CN
multiplicity 2
1 C u1 p0 c0  {2,T}
2 N u0 p1 c0  {1,T}
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
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    reactant1 = 
"""
CN
multiplicity 2
1 C u1 p0 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    reactant2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
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
        A = (8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7460, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    reactant1 = 
"""
CN
multiplicity 2
1 C u1 p0 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-440, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    reactant1 = 
"""
CN
multiplicity 2
1 C u1 p0 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    reactant2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (295000, 'cm^3/(mol*s)'),
        n = 2.45,
        Ea = (2240, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    reactant1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    reactant1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    reactant1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
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
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
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
        A = (2.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    reactant1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    reactant1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
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
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 194,
    reactant1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
N2O
1 N u0 p0 c+1 {2,D} {3,D}
2 N u0 p2 c-1 {1,D}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+17, 'cm^3/(mol*s)'),
        n = -1.52,
        Ea = (740, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 195,
    reactant1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
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
        A = (3.8e+18, 'cm^3/(mol*s)'),
        n = -2,
        Ea = (800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 196,
    reactant1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20300, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (4980, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    reactant1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5070, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (4980, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    reactant1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
CN
multiplicity 2
1 C u1 p0 c0  {2,T}
2 N u0 p1 c0  {1,T}
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
        A = (3.91e+09, 'cm^3/(mol*s)'),
        n = 1.58,
        Ea = (26600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    reactant1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
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
HOCN
1 O u0 p2 c0  {2,S} {3,S}
2 C u0 p0 c0  {1,S} {4,T}
3 H u0 p0 c0  {1,S}
4 N u0 p1 c0  {2,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+06, 'cm^3/(mol*s)'),
        n = 2.03,
        Ea = (13370, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 200,
    reactant1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
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
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4400, 'cm^3/(mol*s)'),
        n = 2.26,
        Ea = (6400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 201,
    reactant1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
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
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
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
        A = (160, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (9000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 N u1 p1 c0  {1,D}
""",
    reactant2 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 203,
    reactant1 = 
"""
C(T)
multiplicity 3
1 C u4 p0 c0 
""",
    reactant2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product1 = 
"""
CN
multiplicity 2
1 C u1 p0 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (46020, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    reactant1 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.12e+09, 'cm^3/(mol*s)'),
        n = 0.88,
        Ea = (20130, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    reactant1 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (74000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    reactant1 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (65000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    reactant1 = 
"""
C(T)
multiplicity 3
1 C u4 p0 c0 
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
CN
multiplicity 2
1 C u1 p0 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    reactant1 = 
"""
C(T)
multiplicity 3
1 C u4 p0 c0 
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    reactant1 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    reactant1 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.62e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    reactant1 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.46e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    reactant1 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+17, 'cm^3/(mol*s)'),
        n = -1.38,
        Ea = (1270, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    reactant1 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
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
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+14, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (760, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    reactant1 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HCNO
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u0 p3 c-1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+13, 'cm^3/(mol*s)'),
        n = -0.36,
        Ea = (580, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    reactant1 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+17, 'cm^3/(mol*s)'),
        n = -1.38,
        Ea = (1270, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    reactant1 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
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
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+14, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (760, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    reactant1 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HCNO
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u0 p3 c-1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+13, 'cm^3/(mol*s)'),
        n = -0.36,
        Ea = (580, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
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
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
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
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
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
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 N u1 p1 c0  {1,D}
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
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (21750, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    reactant1 = 
"""
HCNN
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 N u1 p2 c-1 {2,S}
""",
    reactant2 = 
"""
O(T)
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
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    reactant1 = 
"""
HCNN
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 N u1 p2 c-1 {2,S}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    reactant1 = 
"""
HCNN
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 N u1 p2 c-1 {2,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product3 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    reactant1 = 
"""
HCNN
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 N u1 p2 c-1 {2,S}
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product3 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    reactant1 = 
"""
HCNN
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 N u1 p2 c-1 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    reactant1 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
        A = (9.8e+07, 'cm^3/(mol*s)'),
        n = 1.41,
        Ea = (8500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    reactant1 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+08, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (44000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    reactant1 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
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
        A = (2.2e+06, 'cm^3/(mol*s)'),
        n = 2.11,
        Ea = (11400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    reactant1 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
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
        A = (2.25e+07, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (3800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    reactant1 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
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
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (105000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (13300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 230,
    reactant1 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
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
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
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
        A = (3.3e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 231,
    reactant1 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
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
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
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
        A = (3.3e+06, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 232,
    reactant1 = 
"""
HCNO
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u0 p3 c-1 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+15, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (2850, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 233,
    reactant1 = 
"""
HCNO
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u0 p3 c-1 {2,S}
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
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+11, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (2120, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 234,
    reactant1 = 
"""
HCNO
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u0 p3 c-1 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
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
        A = (1.7e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (2890, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    reactant1 = 
"""
HOCN
1 O u0 p2 c0  {2,S} {3,S}
2 C u0 p0 c0  {1,S} {4,T}
3 H u0 p0 c0  {1,S}
4 N u0 p1 c0  {2,T}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    reactant1 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HCNO
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u0 p3 c-1 {2,S}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 237,
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
N
multiplicity 4
1 N u3 p1 c0 
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 N u1 p1 c0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.1e+14, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (290, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 238,
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
N
multiplicity 4
1 N u3 p1 c0 
""",
    product1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+12, 'cm^3/(mol*s)'),
        n = 0.15,
        Ea = (-90, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    reactant1 = 
"""
NH3
1 N u0 p1 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
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
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
        A = (540000, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (9915, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    reactant1 = 
"""
NH3
1 N u0 p1 c0  {2,S} {3,S} {4,S}
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
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
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
    kinetics = Arrhenius(
        A = (5e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (955, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    reactant1 = 
"""
NH3
1 N u0 p1 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N u1 p1 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
        A = (9.4e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6460, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 242,
    reactant1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14350, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 243,
    reactant1 = 
"""
CN
multiplicity 2
1 C u1 p0 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    reactant2 = 
"""
NO2
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.16e+15, 'cm^3/(mol*s)'),
        n = -0.752,
        Ea = (345, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 244,
    reactant1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
NO2
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
N2O
1 N u0 p0 c+1 {2,D} {3,D}
2 N u0 p2 c-1 {1,D}
3 O u0 p2 c0  {1,D}
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
        A = (3.25e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-705, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 245,
    reactant1 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    reactant2 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 246,
    reactant1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.37e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 247,
    reactant1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+06, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (220, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    reactant1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
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
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH3CHO
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 O u0 p2 c0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.096e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 250,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8e+09, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-1755, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    reactant1 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product3 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    reactant1 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    reactant1 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
H
multiplicity 2
1 H u1 p0 c0 
""",
    product3 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10989, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    reactant1 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.82e+10, 'cm^3/(mol*s)'),
        n = 0.25,
        Ea = (-935, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
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
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product2 = 
"""
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.03e+11, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (11, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
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
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    product2 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.337e+06, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-384, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 257,
    reactant1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
CH3CHO
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 O u0 p2 c0  {2,D}
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
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1808, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    reactant1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
CH3CHO
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 O u0 p2 c0  {2,D}
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
CH3
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.92e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1808, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 259,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH3CHO
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 O u0 p2 c0  {2,D}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
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
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (39150, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 260,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH3CHO
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 O u0 p2 c0  {2,D}
""",
    product1 = 
"""
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
""",
    product2 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2405, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 261,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH3CHO
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 O u0 p2 c0  {2,D}
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
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2405, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 262,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH3CHO
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 O u0 p2 c0  {2,D}
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
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.343e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 263,
    reactant1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH3CHO
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 O u0 p2 c0  {2,D}
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
H2O2
1 O u0 p2 c0  {2,S} {3,S}
2 O u0 p2 c0  {1,S} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11923, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 264,
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
CH3CHO
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 O u0 p2 c0  {2,D}
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
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product3 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.72e+06, 'cm^3/(mol*s)'),
        n = 1.77,
        Ea = (5920, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 265,
    reactant1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product3 = 
"""
CO2
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 266,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
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
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product3 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.81e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 267,
    reactant1 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    reactant2 = 
"""
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
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
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product3 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.35e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 268,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
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
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
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
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 270,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
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
CH2CO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u0 p2 c0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 271,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product2 = 
"""
CH2OH
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 O u0 p2 c0  {1,S} {5,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 272,
    reactant1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    reactant2 = 
"""
O(T)
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
        arrheniusLow = Arrhenius(A=(1.2e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 15.4, '[H][H]': 2.4, '[C]=O': 1.75, '[Ar]': 0.83},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 273,
    reactant1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
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
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 274,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.8e+18, 'cm^6/(mol^2*s)'),
            n = -0.86,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 1.5, 'CC': 1.5, 'O': 0, '[O][O]': 0, 'N#N': 0, '[C]=O': 0.75, '[Ar]': 0},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 275,
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
        arrheniusLow = Arrhenius(A=(1e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 0, 'CC': 3, 'O': 0, '[H][H]': 0, '[Ar]': 0.63},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 276,
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
        arrheniusLow = Arrhenius(A=(2.2e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 0.73, 'O': 3.65, '[Ar]': 0.38},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 277,
    reactant1 = 
"""
HCO
multiplicity 2
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
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
            Ea = (17000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 0, '[H][H]': 2, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 278,
    reactant1 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    reactant2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    product1 = 
"""
NO2
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.06e+20, 'cm^6/(mol^2*s)'),
            n = -1.41,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 279,
    reactant1 = 
"""
NNH
multiplicity 2
1 N u0 p1 c0  {2,D} {3,S}
2 N u1 p1 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.3e+14, 'cm^3/(mol*s)'),
            n = -0.11,
            Ea = (4980, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 280,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N u1 p1 c0  {2,D}
2 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
HNO
1 N u0 p1 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.48e+19, 'cm^6/(mol^2*s)'),
            n = -1.32,
            Ea = (740, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 281,
    reactant1 = 
"""
NCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p1 c0  {1,T}
3 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
N
multiplicity 4
1 N u3 p1 c0 
""",
    product2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(54050, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    reactant1 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    product1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    product2 = 
"""
CN
multiplicity 2
1 C u1 p0 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.04e+29, 'cm^3/(mol*s)'),
            n = -3.3,
            Ea = (126600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 283,
    reactant1 = 
"""
HNCO
1 N u0 p1 c0  {2,D} {3,S}
2 C u0 p0 c0  {1,D} {4,D}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {2,D}
""",
    product1 = 
"""
NH
multiplicity 1
1 N u2 p1 c0  {2,S}
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
        arrheniusLow = Arrhenius(A=(1.18e+16, 'cm^3/(mol*s)'), n=0, Ea=(84720, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 284,
    reactant1 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
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
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.8e+10, 'cm^3/(mol*s)'), n=0, Ea=(2385, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.02e+14, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (3000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.5, 'CC': 3, 'O': 6, '[H][H]': 2, '[O][O]': 6, '[C]=O': 1.5, '[Ar]': 0.5},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 285,
    reactant1 = 
"""
N2O
1 N u0 p0 c+1 {2,D} {3,D}
2 N u0 p2 c-1 {1,D}
3 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product2 = 
"""
O(T)
multiplicity 3
1 O u2 p2 c0 
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(7.91e+10, 's^-1'), n=0, Ea=(56020, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(6.37e+14, 'cm^3/(mol*s)'), n=0, Ea=(56640, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.625},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 286,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
HCN
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 N u0 p1 c0  {1,T}
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 N u1 p1 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.4e+26, 'cm^6/(mol^2*s)'),
            n = -3.4,
            Ea = (1900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 287,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH2(T)
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.04e+26, 'cm^6/(mol^2*s)'),
            n = -2.76,
            Ea = (1600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.562,
        T3 = (91, 'K'),
        T1 = (5836, 'K'),
        T2 = (8552, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 288,
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
            A = (1.39e+16, 'cm^3/(mol*s)'),
            n = -0.534,
            Ea = (536, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.62e+33, 'cm^6/(mol^2*s)'),
            n = -4.76,
            Ea = (2440, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2941, 'K'),
        T2 = (6964, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 289,
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
1 C u1 p0 c0  {2,S} {3,D}
2 H u0 p0 c0  {1,S}
3 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.09e+12, 'cm^3/(mol*s)'),
            n = 0.48,
            Ea = (-260, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.47e+24, 'cm^6/(mol^2*s)'),
            n = -2.57,
            Ea = (425, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7824,
        T3 = (271, 'K'),
        T1 = (2755, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 290,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (3600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.27e+32, 'cm^6/(mol^2*s)'),
            n = -4.82,
            Ea = (6530, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7187,
        T3 = (103, 'K'),
        T1 = (1291, 'K'),
        T2 = (4160, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 291,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (2600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.2e+30, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (5560, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.758,
        T3 = (94, 'K'),
        T1 = (1555, 'K'),
        T2 = (4200, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 292,
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
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.055e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(86, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.36e+31, 'cm^6/(mol^2*s)'),
            n = -4.65,
            Ea = (5080, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 293,
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
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 O u1 p2 c0  {1,S}
""",
    product1 = 
"""
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.43e+12, 'cm^3/(mol*s)'),
            n = 0.515,
            Ea = (50, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.66e+41, 'cm^6/(mol^2*s)'),
            n = -7.44,
            Ea = (14080, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 294,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
C2H
multiplicity 2
1 C u0 p0 c0  {2,S} {3,T}
2 H u0 p0 c0  {1,S}
3 C u1 p0 c0  {1,T}
""",
    product1 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.75e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6464,
        T3 = (132, 'K'),
        T1 = (1315, 'K'),
        T2 = (5566, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 295,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
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
        arrheniusHigh = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2400, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.8e+40, 'cm^6/(mol^2*s)'),
            n = -7.27,
            Ea = (7220, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7507,
        T3 = (98.5, 'K'),
        T1 = (1302, 'K'),
        T2 = (4167, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 296,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
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
C2H4
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.08e+12, 'cm^3/(mol*s)'),
            n = 0.27,
            Ea = (280, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3320, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (207.5, 'K'),
        T1 = (2663, 'K'),
        T2 = (6095, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 297,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
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
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (1820, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6e+41, 'cm^6/(mol^2*s)'),
            n = -7.62,
            Ea = (6970, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9753,
        T3 = (210, 'K'),
        T1 = (984, 'K'),
        T2 = (4374, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 298,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
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
            A = (5.21e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6685, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8422,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 299,
    reactant1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product1 = 
"""
CH2O
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 O u0 p2 c0  {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.3e+07, 'cm^3/(mol*s)'),
            n = 1.5,
            Ea = (79600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.07e+27, 'cm^6/(mol^2*s)'),
            n = -3.42,
            Ea = (84350, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 300,
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
        arrheniusHigh = Arrhenius(A=(7.4e+13, 'cm^3/(mol*s)'), n=-0.37, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.3e+18, 'cm^6/(mol^2*s)'),
            n = -0.9,
            Ea = (-1700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7346,
        T3 = (94, 'K'),
        T1 = (1756, 'K'),
        T2 = (5182, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    reactant1 = 
"""
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
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
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.79e+18, 'cm^3/(mol*s)'),
            n = -1.43,
            Ea = (1330, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4e+36, 'cm^6/(mol^2*s)'),
            n = -5.92,
            Ea = (3140, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.412,
        T3 = (195, 'K'),
        T1 = (5900, 'K'),
        T2 = (6394, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    reactant1 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product1 = 
"""
HCCO
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 O u1 p2 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.69e+28, 'cm^6/(mol^2*s)'),
            n = -3.74,
            Ea = (1936, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5757,
        T3 = (237, 'K'),
        T1 = (1652, 'K'),
        T2 = (5069, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 303,
    reactant1 = 
"""
CH2(T)
multiplicity 3
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.1e+11, 'cm^3/(mol*s)'), n=0.5, Ea=(4510, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.69e+33, 'cm^6/(mol^2*s)'),
            n = -5.11,
            Ea = (7095, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5907,
        T3 = (275, 'K'),
        T1 = (1226, 'K'),
        T2 = (5185, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 304,
    reactant1 = 
"""
CH2(S)
multiplicity 1
1 C u2 p0 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
CH3OH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0  {1,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.82e+17, 'cm^3/(mol*s)'),
            n = -1.16,
            Ea = (1145, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.88e+38, 'cm^6/(mol^2*s)'),
            n = -6.36,
            Ea = (5040, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6027,
        T3 = (208, 'K'),
        T1 = (3922, 'K'),
        T2 = (10180, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 305,
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
            A = (6.77e+16, 'cm^3/(mol*s)'),
            n = -1.18,
            Ea = (654, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.4e+41, 'cm^6/(mol^2*s)'),
            n = -7.03,
            Ea = (2762, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.619,
        T3 = (73.2, 'K'),
        T1 = (1180, 'K'),
        T2 = (9999, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
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
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
C2H2
1 C u0 p0 c0  {2,T} {3,S}
2 C u0 p0 c0  {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(86770, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.58e+51, 'cm^3/(mol*s)'),
            n = -9.3,
            Ea = (97800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7345,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 307,
    reactant1 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
N2
1 N u0 p1 c0  {2,T}
2 N u0 p1 c0  {1,T}
""",
    product1 = 
"""
HCNN
multiplicity 2
1 C u0 p0 c0  {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0  {1,S}
4 N u1 p2 c-1 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.1e+12, 'cm^3/(mol*s)'), n=0.15, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.3e+25, 'cm^6/(mol^2*s)'),
            n = -3.16,
            Ea = (740, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.667,
        T3 = (235, 'K'),
        T1 = (2117, 'K'),
        T2 = (4536, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 1},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 308,
    reactant1 = 
"""
CH
multiplicity 4
1 C u3 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
H2
1 H u0 p0 c0  {2,S}
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.97e+12, 'cm^3/(mol*s)'),
            n = 0.43,
            Ea = (-370, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.82e+25, 'cm^6/(mol^2*s)'),
            n = -2.8,
            Ea = (590, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.578,
        T3 = (122, 'K'),
        T1 = (2535, 'K'),
        T2 = (9365, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 309,
    reactant1 = 
"""
H
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
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
CH2CHO
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 C u0 p0 c0  {1,D} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
6 O u1 p2 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.865e+11, 'cm^3/(mol*s)'),
            n = 0.422,
            Ea = (-1755, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.012e+42, 'cm^6/(mol^2*s)'),
            n = -7.63,
            Ea = (3854, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.465,
        T3 = (201, 'K'),
        T1 = (1773, 'K'),
        T2 = (5333, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
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
    product1 = 
"""
C3H8
1  C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2  H u0 p0 c0  {1,S}
3  H u0 p0 c0  {1,S}
4  H u0 p0 c0  {1,S}
5  C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
6  H u0 p0 c0  {5,S}
7  H u0 p0 c0  {5,S}
8  C u0 p0 c0  {5,S} {9,S} {10,S} {11,S}
9  H u0 p0 c0  {8,S}
10 H u0 p0 c0  {8,S}
11 H u0 p0 c0  {8,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.43e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.71e+74, 'cm^6/(mol^2*s)'),
            n = -16.82,
            Ea = (13065, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.1527,
        T3 = (291, 'K'),
        T1 = (2742, 'K'),
        T2 = (7748, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from GRI-Mech3.0-N.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

