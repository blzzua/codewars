# https://www.codewars.com/kata/5839c48f0cf94640a20001d3

import numpy as np
def land_perimeter(arr):
    nfield = [[1 if c == 'X' else 0 for c in line] for line in arr]
    a = np.array(nfield)
    a = np.pad(a, 1, mode='constant', constant_values=False)
    p = np.sum(a[:,1:] != a[:,:-1]) + np.sum(a[1:,:] != a[:-1,:])
    return f'Total land perimeter: {p}'
