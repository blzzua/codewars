# https://www.codewars.com/kata/525e5a1cb735154b320002c8

import math
def triangular(n):
    if n < 1: return 0
    return math.comb(n+1, 2)

