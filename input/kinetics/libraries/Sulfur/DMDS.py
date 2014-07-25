#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/DMDS"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    reactant1 = 
"""
C2H5SJ1
multiplicity 2
1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 S u0 p2 c0  {1,S} {8,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {2,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {3,S}
""",
    product1 = 
"""
C2H5SJ2
multiplicity 2
1 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {1,S} {3,S} {7,S} {8,S}
3 S u1 p2 c0  {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (85.5, 's^-1'),
        n = 3.04,
        Ea = (11.62, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/DMDS.\nsmall molecule oxidation library, reaction file, version 2, JS, August 6, 2003\noriginally from Leeds methane oxidation mechanism v1.5\nhttp://www.chem.leeds.ac.uk/Combustion/Combustion.html\nfix bug for O2 + HCO = HO2 + CO 1.52E13 0.00 -7.09, change E into positive, change A into 5.12E13 according to NIST\nOntbinding DMDS',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
small molecule oxidation library, reaction file, version 2, JS, August 6, 2003
originally from Leeds methane oxidation mechanism v1.5
http://www.chem.leeds.ac.uk/Combustion/Combustion.html
fix bug for O2 + HCO = HO2 + CO 1.52E13 0.00 -7.09, change E into positive, change A into 5.12E13 according to NIST




Ontbinding DMDS
""",
)

entry(
    index = 2,
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
SH
multiplicity 2
1 S u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    product1 = 
"""
C2H5SJ2
multiplicity 2
1 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0  {1,S} {3,S} {7,S} {8,S}
3 S u1 p2 c0  {2,S}
4 H u0 p0 c0  {1,S}
5 H u0 p0 c0  {1,S}
6 H u0 p0 c0  {1,S}
7 H u0 p0 c0  {2,S}
8 H u0 p0 c0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9960, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/DMDS.',
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
SJJ
multiplicity 1
1 S u2 p2 c0 
""",
    reactant2 = 
"""
SJJ
multiplicity 1
1 S u2 p2 c0 
""",
    product1 = 
"""
S2
multiplicity 3
1 S u1 p2 c0  {2,S}
2 S u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+11, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (-0.88, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur/DMDS.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

