# https://www.codewars.com/kata/59e66e48fc3c499ec5000103

from math import prod
def solve(arr):
    return prod(len(set(a)) for a in arr)
