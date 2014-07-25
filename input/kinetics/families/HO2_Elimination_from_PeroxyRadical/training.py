#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    reactant1 = 
"""
multiplicity 2
1 *1 C u0 p0 c0  {2,S} {4,S} {7,S} {8,S}
2 *2 C u0 p0 c0  {1,S} {3,S} {5,D}
3 *3 O u0 p2 c0  {2,S} {6,S}
4 *5 H u0 p0 c0  {1,S}
5    O u0 p2 c0  {2,D}
6 *4 O u1 p2 c0  {3,S}
7    H u0 p0 c0  {1,S}
8    H u0 p0 c0  {1,S}
""",
    product1 = 
"""
1 *1 C u0 p0 c0  {2,D} {4,S} {5,S}
2 *2 C u0 p0 c0  {1,D} {3,D}
3    O u0 p2 c0  {2,D}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
""",
    product2 = 
"""
multiplicity 2
1 *4 O u0 p2 c0  {2,S} {3,S}
2 *5 H u0 p0 c0  {1,S}
3 *3 O u1 p2 c0  {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.6e+09, 's^-1', '*|/', 2.51189),
        n = 1.2,
        Ea = (34.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["J. W. Allen", "C. F. Goldsmith", "W. H. Green"],
        title = u'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "???",
        pages = """???-???""",
        year = "2011 (accepted)",
    ),
    referenceType = "theory",
    shortDesc = u"""CFG VTST calculations at RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level""",
    longDesc = 
u"""
Quantum chemistry calculations at the RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level
using Gaussian 03 and MOLPRO. High-pressure-limit rate coefficient computed
using Variflex.
""",
)

