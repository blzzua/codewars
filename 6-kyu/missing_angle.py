# https://www.codewars.com/kata/58417e9ab9c25c774500001f

from math import atan, pi
def missing_angle(h, a, o):
    if o == 0:    
        o = (h**2 - a**2)**0.5
    if a == 0:    
        a = (h**2 - o**2)**0.5
    return round(atan(o/a)*180/pi)
