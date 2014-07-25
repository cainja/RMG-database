#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/Thial_Hydrolysis"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    reactant1 = 
"""
CH2S
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 S u0 p2 c0  {1,D}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
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
CH2OHSH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 S u0 p2 c0  {1,S} {6,S}
3 O u0 p2 c0  {1,S} {7,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (960, 'cm^3/(mol*s)'),
        n = 2.43,
        Ea = (28.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.',
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
CH3CHS
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 S u0 p2 c0  {1,D}
3 C u0 p0 c0  {1,S} {5,S} {6,S} {7,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {3,S}
6 H u0 p0 c0  {3,S}
7 H u0 p0 c0  {3,S}
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
CHCH3OHSH
1  C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  S u0 p2 c0  {1,S} {9,S}
4  O u0 p2 c0  {1,S} {10,S}
5  H u0 p0 c0  {1,S}
6  H u0 p0 c0  {2,S}
7  H u0 p0 c0  {2,S}
8  H u0 p0 c0  {2,S}
9  H u0 p0 c0  {3,S}
10 H u0 p0 c0  {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15.4, 'cm^3/(mol*s)'),
        n = 2.78,
        Ea = (27.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.',
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
CH2OHSJ
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 S u1 p2 c0  {1,S}
3 O u0 p2 c0  {1,S} {6,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {3,S}
""",
    product1 = 
"""
CHOHS
1 C u0 p0 c0  {2,S} {3,D} {4,S}
2 O u0 p2 c0  {1,S} {5,S}
3 S u0 p2 c0  {1,D}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
HJ
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+08, 's^-1'),
        n = 1.64,
        Ea = (34.58, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.',
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
CHCH3OHSJ
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3 S u1 p2 c0  {1,S}
4 O u0 p2 c0  {1,S} {9,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {2,S}
9 H u0 p0 c0  {4,S}
""",
    product1 = 
"""
CHOHS
1 C u0 p0 c0  {2,S} {3,D} {4,S}
2 O u0 p2 c0  {1,S} {5,S}
3 S u0 p2 c0  {1,D}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product2 = 
"""
CH3J
multiplicity 2
1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.09e+10, 's^-1'),
        n = 1.02,
        Ea = (29.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.',
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
CHOHS
1 C u0 p0 c0  {2,S} {3,D} {4,S}
2 O u0 p2 c0  {1,S} {5,S}
3 S u0 p2 c0  {1,D}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {2,S}
""",
    product1 = 
"""
CHOSH
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 S u0 p2 c0  {1,S} {5,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+12, 's^-1'),
        n = 0.13,
        Ea = (28.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.',
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
CHOSJ
multiplicity 2
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 S u1 p2 c0  {1,S}
4 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
COS
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 S u0 p2 c0  {1,D}
""",
    product2 = 
"""
HJ
multiplicity 2
1 H u1 p0 c0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.81e+09, 's^-1'),
        n = 1.13,
        Ea = (17.98, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.',
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
COS
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 S u0 p2 c0  {1,D}
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
CSOHOH
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 O u0 p2 c0  {1,S} {5,S}
3 O u0 p2 c0  {1,S} {6,S}
4 S u0 p2 c0  {1,D}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.16, 'cm^3/(mol*s)'),
        n = 3.67,
        Ea = (27.56, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.\n1st pathway, 1st step 53.85 w/o catalysis',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
1st pathway, 1st step 53.85 w/o catalysis
""",
)

entry(
    index = 8,
    reactant1 = 
"""
CSOHOH
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 O u0 p2 c0  {1,S} {5,S}
3 O u0 p2 c0  {1,S} {6,S}
4 S u0 p2 c0  {1,D}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {3,S}
""",
    product1 = 
"""
COSHOH
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 S u0 p2 c0  {1,S} {5,S}
3 O u0 p2 c0  {1,S} {6,S}
4 O u0 p2 c0  {1,D}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.13e+15, 's^-1'),
        n = -0.65,
        Ea = (28.98, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.',
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
COSHOH
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 S u0 p2 c0  {1,S} {5,S}
3 O u0 p2 c0  {1,S} {6,S}
4 O u0 p2 c0  {1,D}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {3,S}
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
H2S
1 S u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.25e+13, 's^-1'),
        n = -0.09,
        Ea = (37.78, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.',
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
COS
1 C u0 p0 c0  {2,D} {3,D}
2 O u0 p2 c0  {1,D}
3 S u0 p2 c0  {1,D}
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
COSHOH
1 C u0 p0 c0  {2,S} {3,S} {4,D}
2 S u0 p2 c0  {1,S} {5,S}
3 O u0 p2 c0  {1,S} {6,S}
4 O u0 p2 c0  {1,D}
5 H u0 p0 c0  {2,S}
6 H u0 p0 c0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13, 'cm^3/(mol*s)'),
        n = 3.35,
        Ea = (25.79, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.\n2nd pathway, 1st step 43.86 w/o catalysis',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
2nd pathway, 1st step 43.86 w/o catalysis
""",
)

entry(
    index = 11,
    reactant1 = 
"""
H2S
1 S u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
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
CH2OHSH
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 S u0 p2 c0  {1,S} {6,S}
3 O u0 p2 c0  {1,S} {7,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50.2, 'cm^3/(mol*s)'),
        n = 3.01,
        Ea = (38.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.\n3rd pathway, form aldehyde from first product (reverse)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
3rd pathway, form aldehyde from first product (reverse)
""",
)

entry(
    index = 12,
    reactant1 = 
"""
H2S
1 S u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
CH3CHO
1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 O u0 p2 c0  {1,D}
3 C u0 p0 c0  {1,S} {5,S} {6,S} {7,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {3,S}
6 H u0 p0 c0  {3,S}
7 H u0 p0 c0  {3,S}
""",
    product1 = 
"""
CHCH3OHSH
1  C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  S u0 p2 c0  {1,S} {9,S}
4  O u0 p2 c0  {1,S} {10,S}
5  H u0 p0 c0  {1,S}
6  H u0 p0 c0  {2,S}
7  H u0 p0 c0  {2,S}
8  H u0 p0 c0  {2,S}
9  H u0 p0 c0  {3,S}
10 H u0 p0 c0  {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (46.9, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (37.1, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/Thial_Hydrolysis.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

