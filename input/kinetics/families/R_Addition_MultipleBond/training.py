#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    reactant1 = 
"""
1 *1 C u0 p0 c0  {2,T} {3,S}
2 *2 C u0 p0 c0  {1,T} {4,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {2,S}
""",
    reactant2 = 
"""
multiplicity 2
1     C u0 p0 c0  {4,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {4,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0  {4,S} {11,S} {12,S} {13,S}
4  *3 C u1 p0 c0  {1,S} {2,S} {3,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
""",
    product1 = 
"""
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5  *1 C u0 p0 c0  {1,S} {6,D} {16,S}
6  *2 C u1 p0 c0  {5,D} {17,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.31, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (493, 'K'),
    ),
    reference = Article(
        authors = ["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals',
        journal = "J. Chem. Soc.",
        pages = """940-944""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962GAR/TRO940-944:1",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Dominguez et al. Data derived from fitting to a complex mechanism.
Pressure 0.01-0.32 atm. Excitation : direct photolysis, analysis : GC. 
C2H2 + Tert-C4H9 --> (CH3)3CCH=CH

Was in the rules database with rank=4. Richard moved to the training database and checked with NIST database. NIST squib: 1962GAR/TRO940-944
A=5.01e+10 cm^3/(mol*s) is the full rate; NB the degeneracy=2 so the per-site rate is half this.
""",
)

entry(
    index = 2,
    reactant1 = 
"""
multiplicity 2
1 *1 C u0 p0 c0  {2,S} {3,S} {5,D}
2 *2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 *3 O u0 p2 c0  {1,S} {4,S}
4    O u0 p2 c0  {3,S} {8,S}
5    O u0 p2 c0  {1,D}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {4,S}
""",
    product1 = 
"""
1 *2 C u0 p0 c0  {2,D} {4,S} {5,S}
2 *1 C u0 p0 c0  {1,D} {3,D}
3    O u0 p2 c0  {2,D}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
""",
    product2 = 
"""
multiplicity 2
1    O u0 p2 c0  {2,S} {3,S}
2 *3 O u1 p2 c0  {1,S}
3    H u0 p0 c0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+16, 's^-1', '*|/', 2.51189),
        n = -1,
        Ea = (29.5, 'kcal/mol'),
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

