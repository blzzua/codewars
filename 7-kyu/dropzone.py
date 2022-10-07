# https://www.codewars.com/kata/5b6d065a1db5ce9b4c00003c

from math import hypot
def dropzone(p, dropzones):
    def dist(cell):
        return hypot(cell[0]-p[0],cell[1]-p[1])
    return min(dropzones, key=dist)

