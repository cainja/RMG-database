#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CCO/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 588,
    label = "CCO;doublebond",
    group1 = 
"""
1 *1 Cd  u0 {2,D}
2 *2 Cdd u0 {1,D} {3,D}
3    Od  u0 {2,D}
""",
    group2 = "OR{mb_CCO, mb_COC}",
    kinetics = ArrheniusEP(
        A = (6.92e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (43.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Quick et al. [107]""",
    longDesc = 
u"""

""",
)

