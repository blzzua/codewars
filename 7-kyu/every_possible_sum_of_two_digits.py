# https://www.codewars.com/kata/5b4e474305f04bea11000148

from itertools import combinations
def digits(num):
    return [int(a)+int(b) for a,b in combinations(str(num), 2)]
