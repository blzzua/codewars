# https://www.codewars.com/kata/5890579a34a7d44f3b00009e

# math solution

from math import log10, floor
def manipulate(n):
    if n == 0: return 0 # log domain error
    d = int(floor(log10(n)/2+1))
    return (n // (10**d)) * (10**d)
