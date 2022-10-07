# https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a

from itertools import groupby
def solution(stones):
    return sum(len(g) - 1 for g in (list(g) for k, g in groupby(stones)))

