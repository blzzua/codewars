# https://www.codewars.com/kata/60ca2ce44875c5004cda5c74

def calc_distance(path):
    res = 0
    for a,b in zip(path, path[1:]):
        res+= 5 * max([abs(c1 - c2) for c1, c2 in zip(a,b)])
    return res
