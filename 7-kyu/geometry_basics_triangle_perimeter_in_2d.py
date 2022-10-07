# https://www.codewars.com/kata/58e3e62f20617b6d7700120a

from itertools import combinations
def size_len(a,b):
    return ((a.x - b.x ) ** 2 + (a.y - b.y ) ** 2)**0.5
def triangle_perimeter(triangle):
    return sum(size_len(*side) for side in combinations((triangle.a, triangle.b, triangle.c),2))


