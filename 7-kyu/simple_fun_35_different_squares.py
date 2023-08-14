# https://www.codewars.com/kata/588805ca44c7e8c3a100013c

import numpy as np
def different_squares(matrix):
    A = np.array(matrix)
    sx, sy = A.shape
    sx, sy = sx - 1, sy - 1
    matrices2 = set()
    for x in range(sx):
        for y in range(sy):
            matrices2.add(tuple(A[x:x+2,y:y+2].ravel()))
    return len(matrices2)
