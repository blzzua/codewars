# https://www.codewars.com/kata/582c6b7cfb3179eb6e000027

from math import pi, cos, sin, tan, atan, hypot
deg30 = pi/6
deg90 = pi/2
deg60 = pi/3

def zig_zag_camel(d, h):
    d=abs(d)
    angle = atan(h/d)
    if angle <= deg30:
        return hypot(d,h)
    res = 0 
    while h > 1e-09:
        d1 = d
        h1 = tan(deg30) * d1
        h2 = (d1 - h1 * tan(deg90 - angle)) / (tan(deg60) + tan(deg90 - angle))
        d2 = tan(deg60) * h2
        res = res + hypot(d1,h1) + hypot(d2,h2)
        d = d2
        h = h - (h1+h2)
    return res

# clever compact: max((h*2,hypot(d,h)))
