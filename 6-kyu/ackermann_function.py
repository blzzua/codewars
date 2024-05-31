# https://www.codewars.com/kata/53ad69892a27079b34000bd9

from functools import lru_cache

@lru_cache()
def Ackermann(m, n):
    if m == 0: 
        return n + 1
    elif n == 0: 
        return Ackermann(m - 1, 1)
    return Ackermann(m - 1, Ackermann(m, n - 1))


# limited m <= 4 solution: https://en.wikipedia.org/wiki/Ackermann_function
def Ackermann(m, n):
    if m == 0: 
        return n + 1
    if m == 1:
        return n + 2
    if m == 2:
        return 2 * n + 3 
    if m == 3:
        return 2 ** (n + 3) - 3
    if m == 4:
        res = 1
        while n + 3 > 0:
            res = 2 ** res
            n -= 1
        return res - 3
