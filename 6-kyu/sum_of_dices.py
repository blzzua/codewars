# https://www.codewars.com/kata/58ff61d2d6b38ee5270000bc

from functools import lru_cache
def outcome(n, s, k):
    if k == 0:
        return 1
    return recursive(n, s, k)

@lru_cache(64000)
def recursive(n, s, k):
    if k < n or k < 0 or (n == 0 and k > 0):
        return 0
    elif n == 0:
        return 1
    res = 0
    for i in range(1, s+1):
        res += recursive(n-1, s, k-i)
    return res
