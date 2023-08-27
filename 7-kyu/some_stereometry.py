#  https://www.codewars.com/kata/5970915e54c27bd71000007b

from math import pi
def stereometry(r,h):
    r_c = (r ** 2 - h ** 2 ) ** 0.5
    vos = round(4 * pi * r ** 2, 3)
    aoc = round(pi * r_c ** 2, 3)
    poc = round(pi * 2 * r_c, 3)
    return (vos, aoc, poc)
