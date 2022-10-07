# https://www.codewars.com/kata/5a026a9cffe75fbace00007f

from math import tan, pi
def circle_diameter(sides, side_length): 
    return side_length / tan(pi/sides)

