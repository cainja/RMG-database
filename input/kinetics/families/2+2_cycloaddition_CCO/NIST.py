#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CCO/NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "1972BLA/DAV491:1",
    reactant1 = 
"""
1 *1 C u0 p0 c0  {2,D} {4,S} {5,S}
2 *2 C u0 p0 c0  {1,D} {3,D}
3    O u0 p2 c0  {2,D}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
""",
    reactant2 = 
"""
1 *4 C u0 p0 c0  {2,D} {4,S} {5,S}
2 *3 C u0 p0 c0  {1,D} {3,D}
3    O u0 p2 c0  {2,D}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
""",
    product1 = 
"""
1  *1 C u0 p0 c0  {3,S} {4,S} {7,S} {8,S}
2  *4 C u0 p0 c0  {3,S} {4,S} {9,S} {10,S}
3  *2 C u0 p0 c0  {1,S} {2,S} {5,D}
4  *3 C u0 p0 c0  {1,S} {2,S} {6,D}
5     O u0 p2 c0  {3,D}
6     O u0 p2 c0  {4,D}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (178, 'm^3/(mol*s)'),
        n = 0,
        Ea = (73.999, 'kJ/mol', '+|-', 0.74),
        T0 = (1, 'K'),
        Tmin = (498, 'K'),
        Tmax = (596, 'K'),
        Pmin = (800, 'Pa'),
        Pmax = (15300, 'Pa'),
    ),
    reference = Article(
        authors = ["Blake, P.G.", "Davis, H.H."],
        title = u'Kinetics of Dimerisation of Gaseous Keten',
        journal = "J. Appl. Chem. Biotechnol.",
        volume = "22",
        pages = """491""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972BLA/DAV491:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007002
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007002/rk00000001.xml
Bath gas: H2C=C=O
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 2,
    label = "1986VAL/BAI16:2",
    reactant1 = 
"""
1  *1 C u0 p0 c0  {3,S} {4,S} {7,S} {8,S}
2  *4 C u0 p0 c0  {5,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0  {2,S} {17,S} {18,S} {19,S}
6     C u0 p0 c0  {2,S} {20,S} {21,S} {22,S}
7  *2 C u0 p0 c0  {1,S} {2,S} {9,D}
8  *3 C u0 p0 c0  {1,S} {2,S} {10,D}
9     O u0 p2 c0  {7,D}
10    O u0 p2 c0  {8,D}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {6,S}
""",
    product1 = 
"""
1     C u0 p0 c0  {3,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0  {3,S} {9,S} {10,S} {11,S}
3  *1 C u0 p0 c0  {1,S} {2,S} {4,D}
4  *2 C u0 p0 c0  {3,D} {5,D}
5     O u0 p2 c0  {4,D}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
""",
    product2 = 
"""
1     C u0 p0 c0  {3,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0  {3,S} {9,S} {10,S} {11,S}
3  *4 C u0 p0 c0  {1,S} {2,S} {4,D}
4  *3 C u0 p0 c0  {3,D} {5,D}
5     O u0 p2 c0  {4,D}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+13, 's^-1'),
        n = 0,
        Ea = (202.873, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (656, 'K'),
        Tmax = (793, 'K'),
    ),
    reference = Article(
        authors = ["Vala, M.", "Baiardo, J.", "Latham, D.", "Mukherjee, R.", "Pascyz, S."],
        title = u'Fourier transform infrared kinetic study of the thermal decomposition of tetramethyl-1-3-cyclobutanedione and dimethylketene',
        journal = "J. Indian Chem. Soc.",
        volume = "63",
        pages = """16""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986VAL/BAI16:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009168
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009168/rk00000001.xml
Excitation technique: Thermal
Analytical technique: Fourier transform (FTIR)
""",
)

