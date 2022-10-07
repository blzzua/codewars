# https://www.codewars.com/kata/58e3f824a33b52c1dc0001c0

from math import pi

def Circle_str(self):
    return f'Circle(({self.center.x},{self.center.y}), r={self.radius})'
Circle.__str__ =  Circle_str

def circle_area(circle):
    return pi * circle.radius**2

