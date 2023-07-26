# https://www.codewars.com/kata/64127b25114de109258fb6fe

import numpy as np
def reflect(point, line):
    x, y = point
    a, b = line
    if a == 0:
        return (y, 2*(b-x)+x)
    aa = -1/a
    bb = y - aa * x
    xx = (bb - b )/(a - aa)
    yx = a *xx + b
    res = np.array((x,y)) - 2*(np.array((x,y)) - np.array((xx,yx)))
    return tuple(res)
