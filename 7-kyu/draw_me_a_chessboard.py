# https://www.codewars.com/kata/56242b89689c35449b000059

import numpy as np
def chess_board(n, k):
    m = k + (1 - k % 2) 
    a = np.vectorize(lambda i: 'X' if i % 2 else 'O')(np.arange(n*m)).reshape((n,m))
    if k % 2 == 0:
        # its easier to cut exstra column than do math for odd rows
        a = np.delete(a, k ,axis=1)
    return a.tolist()

