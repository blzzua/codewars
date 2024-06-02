# https://www.codewars.com/kata/53a1eac7e0afd3ad3300008b

from functools import lru_cache

@lru_cache(1000)
def f(n):
    if n:
        return n-m(f(n-1))
    else:
        return 1

@lru_cache(1000)
def m(n):
    if n:
        return n-f(m(n-1))
    else:
        return 0

