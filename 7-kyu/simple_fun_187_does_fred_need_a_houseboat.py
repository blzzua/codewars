# https://www.codewars.com/kata/58bf72b02d1c7c18d9000127

from math import hypot, pi, sqrt
def does_fred_need_houseboat(x,y):
    rd, area, res = 0, 0, 0
    dist = hypot(x, y)
    while rd < dist:
        rd = sqrt( (area * 2 + 100)/pi )
        res += 1
        area += 50
    return res
