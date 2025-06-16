# https://www.codewars.com/kata/5864f90473bd9c4b47000057

import numpy as np
def connect_four_place(columns):
    A = np.full((6, 7), '-', dtype='U3')
    for i, col in enumerate(columns):
        val = 'Y' if i%2 == 0 else 'R'
        index = 5 - np.where(A[:, col][::-1] == '-')[0][0]
        A[index,col] = val
    return A.tolist()
