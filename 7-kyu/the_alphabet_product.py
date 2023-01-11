# https://www.codewars.com/kata/63b06ea0c9e1ce000f1e2407

from itertools import combinations
from math import prod

def alphabet(ns):
    ns = sorted(ns)
    for i in combinations(ns, 4):
        tails = ns[:]
        for item in i:
            tails.remove(item)
        if all(prod(p) in tails for p in zip(i, i[1:]+(i[0],) )):
            return i[-1]
