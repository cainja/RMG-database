#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_cyclization/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "XSYJ;YJ;S-RR",
    group1 = "OR{XSR3J, XSR4J, XSR5J, XSR6J, XSR7J}",
    group2 = "OR{CJ, SJ, CJ-3, SJ-3}",
    group3 = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 R  u0 {1,S}
3 *4 R  u0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2e+12, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "XSR3J_S;SsJ-3-Cs;S-HC",
    group1 = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *1 Ss  u0 {2,S} {4,S}
4 *2 R   u0 {3,S}
""",
    group2 = 
"""
1 *3 Ss u1 {2,S}
2 *4 Cs u0 {1,S}
""",
    group3 = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3 *4 C  u0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.42e+09, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (42.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "XSR3J_S;CsJ-3-CsHH;S-HC",
    group1 = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *1 Ss  u0 {2,S} {4,S}
4 *2 R   u0 {3,S}
""",
    group2 = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    group3 = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3 *4 C  u0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.34e+10, 's^-1'),
        n = 0.6,
        alpha = 1,
        E0 = (35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "XSR3J_S;CsJ-3-SsHH;S-HSs",
    group1 = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *1 Ss  u0 {2,S} {4,S}
4 *2 R   u0 {3,S}
""",
    group2 = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Ss u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    group3 = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3 *4 Ss u0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.04e+11, 's^-1'),
        n = 0.5,
        alpha = 2,
        E0 = (40.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "XSR3J_S;SsJ-3-Cs;S-Cs(HHH)C",
    group1 = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *1 Ss  u0 {2,S} {4,S}
4 *2 R   u0 {3,S}
""",
    group2 = 
"""
1 *3 Ss u1 {2,S}
2 *4 Cs u0 {1,S}
""",
    group3 = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  u0 {1,S}
4    H  u0 {2,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (9.65e+11, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (33.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "XSR3J_S;CsJ-3-SsHH;S-Cs(HHH)Ss",
    group1 = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *1 Ss  u0 {2,S} {4,S}
4 *2 R   u0 {3,S}
""",
    group2 = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Ss u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    group3 = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *4 Ss u0 {1,S}
3 *2 Cs u0 {1,S} {4,S} {5,S} {6,S}
4    H  u0 {3,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (1.76e+12, 's^-1'),
        n = 0.2,
        alpha = 0,
        E0 = (34.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "XSR3J_S;CsJ-3-SsHH;S-Ss(H)Ss",
    group1 = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *1 Ss  u0 {2,S} {4,S}
4 *2 R   u0 {3,S}
""",
    group2 = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Ss u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    group3 = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *4 Ss u0 {1,S}
3 *2 Ss u0 {1,S} {4,S}
4    H  u0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (2.65e+12, 's^-1'),
        n = 0.1,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "XSR5J_SSS;CsJ-CsCsH;S-Cs(NonDe)C",
    group1 = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 Ss  u0 {4,S} {6,S}
6 *2 R   u0 {5,S}
""",
    group2 = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    group3 = 
"""
1 *1 Ss     u0 {2,S} {3,S}
2 *2 Cs     u0 {1,S} {4,S} {5,S} {6,S}
3 *4 C      u0 {1,S}
4    [H,Cs] u0 {2,S}
5    [H,Cs] u0 {2,S}
6    [H,Cs] u0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (27000, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (7.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""AA Calc""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "XSR6J_SSSS;CsJ-CsCsH;S-Cs(NonDe)C",
    group1 = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *4 R!H u0 {4,S} {6,S}
6 *1 Ss  u0 {5,S} {7,S}
7 *2 R   u0 {6,S}
""",
    group2 = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    group3 = 
"""
1 *1 Ss     u0 {2,S} {3,S}
2 *2 Cs     u0 {1,S} {4,S} {5,S} {6,S}
3 *4 C      u0 {1,S}
4    [H,Cs] u0 {2,S}
5    [H,Cs] u0 {2,S}
6    [H,Cs] u0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (270, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (6.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""AA Calc""",
    longDesc = 
u"""

""",
)

