# https://www.codewars.com/kata/58bd011fd0efbec33400001f

import numpy as np
def black_hole(n, a, b):
    A = np.zeros((n,n), dtype=int)
    if n % 2 == 1: A[n//2][n//2] = n*n
    cur_value = 0
    for layer in range(n//2):
        for j in range(layer,n-layer-1):  # filling zero row
            curpos = layer                # current position
            for rot in range(4):
                cur_value += 1
                if A[curpos][j] != 0:
                    curpos+=1
                A[curpos][j] = cur_value
                A = np.rot90(A)           # it's easier for me to move the canvas instead of moving the brush
    return A[a][b]
