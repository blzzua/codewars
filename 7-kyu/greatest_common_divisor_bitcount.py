# https://www.codewars.com/kata/54b45c37041df0caf800020f

from math import gcd
def binary_gcd(x, y):
    g = gcd(x, y)
    return bin(g).count('1')
