# https://www.codewars.com/kata/5b56e42805f04b1780000073

from itertools import combinations
import numpy as np
def dist(comb):
    return np.linalg.norm(np.array(comb[0])-np.array(comb[1])).round(2)

def furthest_distance(points):
    return max(map(dist,combinations(points,2)))



