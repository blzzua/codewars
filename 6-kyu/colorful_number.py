# https://www.codewars.com/kata/5441310626bc6a1e61000f2c

from itertools import starmap, repeat, combinations
from operator import getitem
from math import prod

def subslices(iterable): # from more_itertools
    seq = list(iterable)
    slices = starmap(slice, combinations(range(len(seq) + 1), 2))
    return map(getitem, repeat(seq), slices)

def colorful(number):
    seen = set()
    for comb in list(subslices(str(number))):
        test_value = prod(map(int,comb))
        if test_value not in seen:
            seen.add(test_value)
        else:
            return False
    return True
