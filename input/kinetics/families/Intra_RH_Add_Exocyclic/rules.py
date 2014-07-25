#!/usr/bin/env python
# encoding: utf-8

name = "Intra_RH_Add_Exocyclic/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""
entry(
    index = 807,
    label = "Rn;multiplebond_intra;radadd_intra",
    group1 = "OR{R4, R5, R6, R7}",
    group2 = 
"""
1 *2 C     u0 {2,[D,T]}
2 *3 [C,O] u0 {1,[D,T]}
""",
    group3 = 
"""
1 *1 R!H u0
""",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 808,
    label = "R6_SSS_D;double_bond_intra_Nd;radadd_intra_O",
    group1 = 
"""
1 *1 R!H     u0 {2,S} {3,S}
2 *4 H       u0 {1,S}
3 *5 R!H     u0 {1,S} {4,S}
4 *6 R!H     u0 {3,S} {5,S}
5 *7 R!H     u0 {4,S} {6,S}
6 *2 Cd      u0 {5,S} {7,D}
7 *3 [Cd,Od] u0 {6,D}
""",
    group2 = 
"""
1 *2 Cd     u0 {2,D} {3,S}
2 *3 Od     u0 {1,D}
3    [Cs,O] u0 {1,S}
""",
    group3 = 
"""
1 *1 O u0
""",
    kinetics = ArrheniusEP(
        A = (2.51e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (712.954, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

