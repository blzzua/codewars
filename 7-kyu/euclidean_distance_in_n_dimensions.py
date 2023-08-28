# https://www.codewars.com/kata/595877be60d17855980013d3

from math import hypot
def euclidean_distance(point1, point2):
    return round(hypot(*[abs(a-b) for a,b in zip(point1, point2)]),2)
