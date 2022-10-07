# https://www.codewars.com/kata/570409d3d80ec699af001bf9

from functools import lru_cache

@lru_cache
def fusc(n):
    assert type(n) == int and n >= 0
    if n in (0,1):
        return n
    else:
        return fusc(n//2) + (fusc(n//2 + 1) if  n % 2 else 0)
    

