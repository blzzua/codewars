# https://www.codewars.com/kata/59b166f0a35510270800018d

import scipy.integrate as integrate
def find_area(points):
    res = 0
    for p1, p2 in zip(points,points[1:]):
        a = (p2.Y - p1.Y) / (p2.X - p1.X)
        b = p1.Y - a * p1.X
        res += round(integrate.quad(lambda x: a * x + b,  p1.X, p2.X)[0],1)
    return res
