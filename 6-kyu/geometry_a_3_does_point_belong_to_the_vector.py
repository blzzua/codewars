# https://www.codewars.com/kata/554e5ef27daf4082f6000071

from preloaded import vector_length, point_vs_vector_v2
epsilon = 6

from math import dist
def point_in_vector(point, vector):
    a = dist(point, vector[0])
    b = dist(point, vector[1])
    c = dist(vector[0], vector[1])
    return round(c, epsilon) == round(a + b, epsilon)
