# https://www.codewars.com/kata/53ad69892a27079b34000bd9

from functools import lru_cache

@lru_cache()
def Ackermann(m, n):
    if m == 0: 
        return n + 1
    elif n == 0: 
        return Ackermann(m - 1, 1)
    return Ackermann(m - 1, Ackermann(m, n - 1))

