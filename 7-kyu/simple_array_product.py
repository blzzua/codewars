# https://www.codewars.com/kata/5d0365accfd09600130a00c9

from math import prod
from itertools import product
def solve(arr):
    return max(prod(c) for c in product(*arr))

