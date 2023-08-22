# https://www.codewars.com/kata/5b01abb9de4c7f3c22000012

from math import hypot

def ellipse_contains_point(f0, f1, l, p): 
    p0 = hypot( p['x'] - f0['x'], p['y'] - f0['y']) 
    p1 = hypot( p['x'] - f1['x'], p['y'] - f1['y']) 
    return p0 + p1 <= l
