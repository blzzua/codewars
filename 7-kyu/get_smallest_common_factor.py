# https://www.codewars.com/kata/5933af2db328fbc731000010

from math import gcd
from itertools import combinations
from gmpy2 import next_prime

def scf (arr):
    p = 1
    max_item = max(arr, default = 1)
    while p < max_item:
        p = next_prime(p)
        if all([i % p == 0 for i in arr]):
            return p
    return 1
