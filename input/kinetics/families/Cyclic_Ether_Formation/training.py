#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/training"
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
1 *1 C u1 p0 c0  {3,S} {6,S} {7,S}
2    O u0 p2 c0  {3,D}
3 *4 C u0 p0 c0  {1,S} {2,D} {4,S}
4 *2 O u0 p2 c0  {3,S} {5,S}
5 *3 O u0 p2 c0  {4,S} {8,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {1,S}
8    H u0 p0 c0  {5,S}
""",
    product1 = 
"""
1 *1 C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2 *4 C u0 p0 c0  {1,S} {3,S} {4,D}
3 *2 O u0 p2 c0  {1,S} {2,S}
4    O u0 p2 c0  {2,D}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
""",
    product2 = 
"""
multiplicity 2
1 *3 O u1 p2 c0  {2,S}
2    H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+17, 's^-1', '*|/', 2.51189),
        n = -1.1,
        Ea = (27.2, 'kcal/mol'),
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

