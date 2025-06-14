# https://www.codewars.com/kata/55a7de09273f6652b200002e

import sys
from functools import lru_cache
sys.setrecursionlimit(10000)

@lru_cache(500000)
def L(n):
    if n < 0:
        return L(n+2) - L(n+1)
    if n == 0:
        return 2
    if n == 1:
        return 1
    return L(n-1) + L(n-2)

def lucasnum(n):
    return L(n)


# iterative
    l1, l2 = 2, 1
    for _ in range(abs(n)):
        l1, l2 = l2, l1 + l2
    return l1 * sing(n)
