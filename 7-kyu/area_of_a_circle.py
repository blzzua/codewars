# https://www.codewars.com/kata/537baa6f8f4b300b5900106c

from math import pi
def circle_area(r):
    if type(r) in (float,int) and r >= 0:
        return round(pi*r*r, 2)
    return False
        

