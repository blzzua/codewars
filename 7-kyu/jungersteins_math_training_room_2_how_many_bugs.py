# https://www.codewars.com/kata/58cf479f87c2e967250000e4

from math import modf

def cal_n_bug(n_head, n_leg, n_wing):
    s =  1/2 * (n_leg - 6 * n_head) 
    d = n_wing + s - n_head
    b = n_head - s - d
    if (s < 0 or b < 0 or d < 0) or sum(modf(c)[0] for c in [s, b, d]) > 0:
        s = b = d = -1
    return [s, b, d]
