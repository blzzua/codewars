# https://www.codewars.com/kata/5612ab201830eb000f0000c0

from functools import lru_cache
from gmpy2 import is_divisible, isqrt
from itertools import count 

@lru_cache
def div_num(x):
    res = 0
    for i in range(1, isqrt(x) + 1):
        if is_divisible(x, i):
            res += 1
            if x // i != i:
                res += 1
    return res
def find_min_num(num_div):
    return next(filter(lambda x: div_num(x) == num_div, count(1)))

