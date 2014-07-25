#!/usr/bin/env python
# encoding: utf-8

name = "Glarborg/C0"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
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
O
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
        A = (3.6e+15, 'cm^3/(mol*s)'),
        n = -0.41,
        Ea = (16600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
        A = (1e+17, 'cm^6/(mol^2*s)'),
        n = -0.6,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
        A = (1e+19, 'cm^6/(mol^2*s)'),
        n = -1,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
O
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(19175, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
        A = (4300, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (-1822, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
        A = (2.1e+08, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (3449, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
H2
1 H u0 p0 c0  {2,S}
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
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
        A = (740000, 'cm^3/(mol*s)'),
        n = 2.433,
        Ea = (53502, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
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
        Ea = (400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
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
        A = (1.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
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
        A = (1.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-445, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
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
O2
multiplicity 3
1 O u1 p2 c0  {2,S}
2 O u1 p2 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+13, 'cm^3/(mol*s)', '*|/', 1.58),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1408, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(11034, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
H2O
1 O u0 p2 c0  {2,S} {3,S}
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
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3580, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
        A = (1.7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3760, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
HO2
multiplicity 2
1 O u0 p2 c0  {2,S} {3,S}
2 O u1 p2 c0  {1,S}
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
        A = (9.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(427, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.6e+18, 'cm^3/(mol*s)'), n=0, Ea=(29410, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
2 O u1 p2 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.5e+16, 'cm^6/(mol^2*s)'),
            n = -0.41,
            Ea = (-1116, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2, '[O][O]': 0.78, 'O': 11, 'N#N': 0, '[Ar]': 0},
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
2 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4e+11, 's^-1'), n=0, Ea=(37137, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.291e+16, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (43638, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.5, 'O': 12, '[Ar]': 0.64},
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
        arrheniusLow = Arrhenius(A=(7e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0, 'O': 0, 'N#N': 0},
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
        arrheniusLow = Arrhenius(A=(6.2e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O': 5},
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
            A = (1.9e+13, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[O][O]': 1.5, 'O': 10, 'N#N': 1.5},
        comment = 'Reaction and kinetics from Glarborg/C0.',
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
OH
multiplicity 2
1 O u1 p2 c0  {2,S}
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
H2O
1 O u0 p2 c0  {2,S} {3,S}
2 H u0 p0 c0  {1,S}
3 H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.5e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0.73, 'O': 12, '[Ar]': 0.38},
        comment = 'Reaction and kinetics from Glarborg/C0.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

