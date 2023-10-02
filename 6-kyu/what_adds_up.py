# https://www.codewars.com/kata/53cce49fdf221844de0004bd

from itertools import product
def addsup(a1, a2, a3):
    return [[a,b,c] for a,b,c in product(a1, a2, a3) if a+b == c]
