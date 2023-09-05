# https://www.codewars.com/kata/58989a079c70093f3e00008d

from itertools import product
def cartesian_neighbor(x, y):
    return [(x+a,y+b) for a, b in product([-1,0,1], [-1,0,1]) if not (a == b == 0)]
