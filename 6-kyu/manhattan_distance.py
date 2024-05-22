# https://www.codewars.com/kata/52998bf8caa22d98b800003a

def manhattan_distance(pointA, pointB):
    return sum(abs(a-b) for a, b in zip(pointA, pointB))
