# https://www.codewars.com/kata/56b18992240660a97c00000a

from itertools import permutations
from math import prod
def permutation_average(n):
    return int(round(sum(int(''.join(map(str,p))) for p in permutations(list(map(int,str(n)))))/prod(range(1,len(str(n))+1))))
