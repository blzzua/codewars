# https://www.codewars.com/kata/5b6b128783d648c4c4000129

from math import prod
def smallest_product(a):
    return min(map(prod,a))

