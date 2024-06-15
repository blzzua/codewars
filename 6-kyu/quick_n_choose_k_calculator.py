# https://www.codewars.com/kata/55b22ef242ad87345c0000b2

# my solution
import math
choose=math.comb

# optimized solutions
from math import comb as choose
from gmpy2 import bincoef as choose


# actual algoritmic solution:
def factorial(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return result

def choose(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))
