# https://www.codewars.com/kata/576400f2f716ca816d001614

from math import gcd
def reduce_fraction(f):
    g = gcd(*f)
    return tuple(map(lambda x: x//g,f))


