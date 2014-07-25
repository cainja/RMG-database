#!/usr/bin/env python
# encoding: utf-8

name = "Methylformate"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    reactant1 = 
"""
Mfmt
1 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {7,D} {8,S}
3 O u0 p2 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {2,D}
8 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    product2 = 
"""
CH3OH
1 O u0 p2 c0  {2,S} {3,S}
2 C u0 p0 c0  {1,S} {4,S} {5,S} {6,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {2,S}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.128e+12, 's^-1'),
        n = 0.735,
        Ea = (68.628, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
Mfmt
1 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {7,D} {8,S}
3 O u0 p2 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {2,D}
8 H u0 p0 c0  {2,S}
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
CH2O
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.158e+09, 's^-1'),
        n = 1.28,
        Ea = (75.979, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
Mfmt
1 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {7,D} {8,S}
3 O u0 p2 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {2,D}
8 H u0 p0 c0  {2,S}
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
CH4
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.536e+11, 's^-1'),
        n = 0.832,
        Ea = (83.612, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
Mofml
multiplicity 2
1 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0  {1,S} {3,S}
3 C u1 p0 c0  {2,S} {7,D}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {3,D}
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
CH3j
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+09, 's^-1'),
        n = 1.09,
        Ea = (14.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
CO
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    reactant2 = 
"""
CH3Oj
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
Mofml
multiplicity 2
1 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0  {1,S} {3,S}
3 C u1 p0 c0  {2,S} {7,D}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.97e+09, 'cm^3/(mol*s)'),
        n = 1.27,
        Ea = (5.81, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
HCjO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
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
Fmoml
multiplicity 2
1 C u1 p0 c0  {3,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {4,D} {7,S}
3 O u0 p2 c0  {1,S} {2,S}
4 O u0 p2 c0  {2,D}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5030, 'cm^3/(mol*s)'),
        n = 2.48,
        Ea = (9.32, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
Hj
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
Mfmt
1 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {7,D} {8,S}
3 O u0 p2 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {2,D}
8 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
Mofml
multiplicity 2
1 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0  {1,S} {3,S}
3 C u1 p0 c0  {2,S} {7,D}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (228000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (6.56, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
Hj
multiplicity 2
1 H u1 p0 c0 
""",
    reactant2 = 
"""
Mfmt
1 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {7,D} {8,S}
3 O u0 p2 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {2,D}
8 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
H2
1 H u0 p0 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product2 = 
"""
Fmoml
multiplicity 2
1 C u1 p0 c0  {3,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {4,D} {7,S}
3 O u0 p2 c0  {1,S} {2,S}
4 O u0 p2 c0  {2,D}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (116000, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (7.62, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
CH3j
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
Mfmt
1 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {7,D} {8,S}
3 O u0 p2 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {2,D}
8 H u0 p0 c0  {2,S}
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
Mofml
multiplicity 2
1 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0  {1,S} {3,S}
3 C u1 p0 c0  {2,S} {7,D}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.34, 'cm^3/(mol*s)'),
        n = 2.82,
        Ea = (6.81, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
CH3j
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
Mfmt
1 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {7,D} {8,S}
3 O u0 p2 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {2,D}
8 H u0 p0 c0  {2,S}
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
Fmoml
multiplicity 2
1 C u1 p0 c0  {3,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {4,D} {7,S}
3 O u0 p2 c0  {1,S} {2,S}
4 O u0 p2 c0  {2,D}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.257, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (8.02, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
CH3Oj
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
HCjO
multiplicity 2
1 C u1 p0 c0  {2,D} {3,S}
2 O u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
Mfmt
1 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {7,D} {8,S}
3 O u0 p2 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {2,D}
8 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
CH3j
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
OjCHO
multiplicity 2
1 O u1 p2 c0  {2,S}
2 C u0 p0 c0  {1,S} {3,D} {4,S}
3 O u0 p2 c0  {2,D}
4 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
Mfmt
1 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {3,S} {7,D} {8,S}
3 O u0 p2 c0  {1,S} {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 O u0 p2 c0  {2,D}
8 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

