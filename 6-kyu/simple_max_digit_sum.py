# https://www.codewars.com/kata/5b162ed4c8c47ea2f5000023

from math import log10, floor
def solve(n):
    power = 10 ** (len(str(n)) - 1)
    last = power * (n // power + 1) - 1
    if last > n + 1:
        return last - 10 ** len((str(last - n)))
    elif last > n:
        return n
    else:
        return last
