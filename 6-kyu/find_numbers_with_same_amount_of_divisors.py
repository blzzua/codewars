# https://www.codewars.com/kata/55f1614853ddee8bd4000014

import math
from functools import lru_cache

@lru_cache(20000)
def divisors_cnt(n):
    res = []
    large_divisors = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            res.append(i)
            if i*i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        res.append(divisor)
    return len(res)

def count_pairs_int(diff, n_max):
    res = []
    for a in range(n_max - diff):
        if divisors_cnt(a) == divisors_cnt(a + diff):
            res.append([a, a + diff])
    return len(res)

