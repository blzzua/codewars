# https://www.codewars.com/kata/57d99f6bbfcdc5b3b0000286

from itertools import combinations

def check_if_triangle_rect(tri):
    a = tri[0]
    b = tri[1]
    c = tri[2]
    ab = (a[0]-b[0], a[1]-b[1])
    ac = (a[0]-c[0], a[1]-c[1])
    bc = (b[0]-c[0], b[1]-c[1])
    for p1, p2 in combinations((ab,ac,bc),2):
        if abs(p1[0]*p2[0] + p1[1]*p2[1]) == 0:
            return True
    return False

def count_rect_triang(points):
    res = 0
    points = list(set((tuple(p) for p in points)))
    for c in combinations( points, 3):
        if check_if_triangle_rect(c):
            res += 1
    return res
