# https://www.codewars.com/kata/56b58d11e3a3a7cade000792

from gmpy2 import is_prime
def sexy_prime(x, y):
    return abs(x - y) == 6 and is_prime(x) and is_prime(y)
