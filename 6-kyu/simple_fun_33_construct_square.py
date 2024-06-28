# https://www.codewars.com/kata/58870c87c81516bbdb0000d8

from collections import Counter
def freq(n):
    return tuple(v[1] for v in Counter(str(n*n)).most_common())

PRECALC = {freq(i): i  for i in range(100_0000)}
    
def construct_square(s):
    target = tuple(v[1] for v in Counter(s).most_common())
    res = 1j
    if target in PRECALC:
        res = PRECALC[target]
    return int((res**2).real)
