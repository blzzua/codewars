# https://www.codewars.com/kata/52de9bd621c71b919c000592

from math import hypot
def in_sphere(coords, radius):
    return hypot(*coords) <= radius
