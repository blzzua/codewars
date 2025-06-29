# https://www.codewars.com/kata/5886dbc685d5788715000071

from functools import lru_cache

@lru_cache(100000)
def s(n):
    return sum(map(int,str(n)))

def comfortable_numbers(l, r):
    res = 0
    for a in range(l, r+1):
        for b in range(a+1, r+1):
            if (b >= a - s(a) and b <= a + s(a)) and (a >= b - s(b) and a <= b + s(b)):
                res += 1
    return res
