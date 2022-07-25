# https://www.codewars.com/kata/57d52a7f76da830e43000188

from math import sqrt
def sctc(sin):
    cos = sqrt(1 - sin * sin)
    tan = sin / cos if cos else None
    cot = cos / sin if sin else None
    return [round(i, 2) for value in (sin, cos, tan, cot) if i is not None]
