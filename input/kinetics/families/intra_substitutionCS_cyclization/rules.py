#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_cyclization/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "XSYJ;YJ;C-RRR;S-R",
    group1 = "OR{XSR3J, XSR4J, XSR5J, XSR6J, XSR7J}",
    group2 = "OR{CJ, SJ, CJ-3, SJ-3}",
    group3 = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *4 R  u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    group4 = 
"""
1 *2 S u0 {2,S}
2    R u0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+12, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
u"""

""",
)

