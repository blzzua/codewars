# https://www.codewars.com/kata/5b8be3ae36332f341e00015e

from itertools import permutations
def solve(s,k):
    return sum(1 for a, b in permutations(s.split(), 2) if int(a+b) % k == 0)
