import numpy as np
def crossing_sum(matrix, row, col):
    A = np.array(matrix)
    return A[:,col].sum() + A[row,:].sum() - A[row,col]
