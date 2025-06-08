# https://www.codewars.com/kata/58952e29f0902eae8b0000cb

import numpy as np

def minesweeper(matrix):
    A = np.matrix(matrix)
    rows, cols = A.shape
    B = np.zeros((rows, cols), dtype=int)
    nd_iterator = np.nditer(A, flags=['multi_index'])
    for value in nd_iterator:
        i, j  = nd_iterator.multi_index
        row_beg = max(0, i-1)
        row_end = min(rows, i+2)
        col_beg = max(0, j-1)
        col_end = min(cols, j+2)
        B[i, j] = np.sum(A[row_beg:row_end, col_beg:col_end]) - (1 if value else 0)
    return B.tolist()

