# https://www.codewars.com/kata/5862e7c63f8628a126000e18

from math import prod
def box_capacity(*d):
    return prod( i*12//16 for i in d)

