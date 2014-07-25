#!/usr/bin/env python
# encoding: utf-8

name = "intra_NO2_ONO_conversion/NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "1981BAT/BUR467:1",
    reactant1 = 
"""
multiplicity 2
1 *2 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *1 O u1 p2 c0  {1,S}
3 *3 H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
""",
    product1 = 
"""
multiplicity 2
1 *1 C u1 p0 c0  {2,S} {4,S} {5,S}
2 *2 O u0 p2 c0  {1,S} {3,S}
3 *3 H u0 p0 c0  {2,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (108.92, 'kJ/mol', '+|-', 9.811),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (473, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Burrows, J.P.", "Robinson, G.N."],
        title = u'On the Isomerisation of the Methoxy Radical: Relevance to Atmospheric Chemistry and Combustion',
        journal = "Chem. Phys. Lett.",
        volume = "78",
        pages = """467""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981BAT/BUR467:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010565
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010565/rk00000001.xml
Rate constant is an upper limit.
Bath gas: N2
""",
)

