# https://www.codewars.com/kata/5830e7feff1a3ce8d4000062

from math import pi
def ellipse(a, b):
    area = round(a * b * pi, 1)
    perimeter = round(pi * ((3/2)*(a+b) - (a*b) ** 0.5),1)
    return f'Area: {area}, perimeter: {perimeter}'
