# https://www.codewars.com/kata/59971206e06bbf4407002382

from math import sqrt

def sum_and_multiply(a, b):
    if a**2 < 4 * b:
        return None
    D = sqrt(a ** 2 - 4 * b)
    x = (a - D )//2
    y = (a + D )//2
    if x+y == a and x*y ==b :
        return [x, y]
