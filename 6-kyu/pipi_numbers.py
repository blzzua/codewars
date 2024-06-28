# https://www.codewars.com/kata/5af27e3ed2ee278c2c0000e2

from functools import lru_cache

@lru_cache(1000)
def pipi(n):
    if n <= 1: 
        return n
    P = n
    for i in range(1, n):
        P = P ** 2 - pipi(i)
    return P ** 2
  
