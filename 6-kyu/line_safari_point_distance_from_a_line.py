# https://www.codewars.com/kata/59c053f070a3b7d19100007e

from math import hypot
def distance_from_line(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    parall_sq = abs((y2 - y1) * x3 - (x2 - x1) * y3 + x2 * y1 - y2 * x1)
    bc_norm = hypot(x2 - x1 , y2 - y1)
    if bc_norm == 0:
        return hypot(x3 - x1 , y3 - y1)
    return parall_sq/bc_norm


# clever from math import dist instead hypot
