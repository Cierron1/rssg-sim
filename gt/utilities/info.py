from math import sin, tan, pi, sqrt
import numpy as np


m = 1/(4*sin(pi/5))
n = 1/(4*tan(pi/5))
s = 1/(2*sin(pi/8))
r2 = sqrt(2)
r3 = sqrt(3)

jelly = {
    1:  np.array((-0.5, +n+m-4.5)),
    2:  np.array(( 0.5, +n+m+2.5)),
    3:  np.array(( 0.5, +n+m-4.5)),
    4:  np.array(( 0.5, +n+m-1.5)),
    5:  np.array(( 0.5, +n+m-0.5)),
    6:  np.array(( n/m, -3*n+2*m-4.5)),
    7:  np.array(( 0.5, +n+m+3.5)),
    8:  np.array((-0.5, +n+m-3.5)),
    9:  np.array(( 0.5, +n+m+4.5)),
    10: np.array(( 0, -n-m-4.5)),
    11: np.array(( 0.5, +n+m+0.5)),
    12: np.array(( 0.5, +n+m-2.5)),
    13: np.array(( 0.5, +n+m-3.5)),
    14: np.array(( 0.5, +n+m+1.5)),
    15: np.array((-n/m, -3*n+2*m-4.5)),
}

totem = {
    1:  np.array((-0.5, -2.5)),
    3:  np.array(( 0.5, -2.5)),
    5:  np.array(( 0.5,  0.5)),
    7:  np.array((-0.5,  0.5)),
    9:  np.array((-0.5,  1.5)),
    11: np.array(( 0.5,  1.5)),
    13: np.array(( 0.5, -3.5)),
    15: np.array((-0.5, -3.5)),
    17: np.array(( 0.5,  4.5)),
    19: np.array((-0.5,  4.5)),
    21: np.array((-1.5, -3.5)),
    23: np.array(( 1.5, -3.5)),
    25: np.array(( 1.5,  1.5)),
    27: np.array((-1.5,  1.5)),
    29: np.array((-0.5, -0.5)),
    31: np.array(( 0.5, -0.5)),
    33: np.array(( 0.5, -1.5)),
    35: np.array((-0.5, -1.5)),
    37: np.array((-1.5,  2.5)),
    39: np.array(( 1.5,  2.5)),
    41: np.array(( 1.5, -1.5)),
    43: np.array((-1.5, -1.5)),
    45: np.array((-0.5,  3.5)),
    47: np.array(( 0.5,  3.5)),
    49: np.array((-0.5, -4.5)),
    51: np.array(( 0.5, -4.5)),
    53: np.array(( 0.5,  2.5)),
    55: np.array((-0.5,  2.5)),
    57: np.array((-1.5,  0.5)),
    59: np.array(( 1.5,  0.5)),
}

jug = {
    2:  np.array((-0.5*r2*s, -0.5*r2*s-1)),
    6:  np.array((0, s-1)),
    10: np.array((0, s)),
    14: np.array((0, -s-1)),
    18: np.array((0, +2+s)),
    22: np.array((0.5*r2*s, -0.5*r2*s-1)),
    26: np.array((-0.5*r3, 0.5+s)),
    30: np.array((-0.5*r2*s, 0.5*r2*s-1)),
    34: np.array((-s,-1)),
    38: np.array((-0.5*r3,1.5+s)),
    42: np.array((s,-1)),
    46: np.array((0.5*r3,1.5+s)),
    50: np.array((0,-s-2)),
    54: np.array((0.5*r3,0.5+s)),
    58: np.array((0.5*r2*s,0.5*r2*s-1))
}


