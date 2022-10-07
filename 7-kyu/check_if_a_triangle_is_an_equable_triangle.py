# https://www.codewars.com/kata/57d0089e05c186ccb600035e

from numpy import prod
def equable_triangle(*t):
    p = sum(t)/2 # half of perimeter used for Heron formula
    sq = prod([(p-i) for i in t]+[p])**0.5
    return sq == p*2


