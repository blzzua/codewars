# https://www.codewars.com/kata/5eaf88f92b679f001423cc66

from math import gcd 

def reflections(max_x, max_y):
    m = gcd(max_x, max_y)
    if ( max_x // m + max_y // m ) % 2 == 0:
        return True
    else:
        return False
