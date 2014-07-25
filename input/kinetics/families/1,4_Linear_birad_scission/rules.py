#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Linear_birad_scission/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "RJJ",
    group1 = 
"""
1 *1 R u1 {2,[S,D]}
2 *2 R u0 {1,[S,D]} {3,S}
3 *3 R u0 {2,S} {4,[S,D]}
4 *4 R u1 {3,[S,D]}
""",
    kinetics = ArrheniusEP(
        A = (5e+12, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""AG Vandeputte estimate (should be fast)""",
    longDesc = 
u"""

""",
)

