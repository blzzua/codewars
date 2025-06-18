# https://www.codewars.com/kata/629e18298f2d21006516e381

from functools import lru_cache
@lru_cache(10000)
def f(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    return sum( f(n-k) for k in range(2, n+1))

def permuts(n):
    return f(n+2)
