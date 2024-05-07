# https://www.codewars.com/kata/59c804d923dacc6c41000004

import numpy as np
def circle(radius):
    if radius < 0:
        return ''
    if radius == 0:
        return '\n'
    n = 2 * radius - 1
    a = np.ndarray((n,n), dtype=object)
    a[:] = ' '
    for i,j in np.ndindex(a.shape):
        if (i-radius+1)**2 + (j-radius+1)** 2 < radius**2:
            a[j,i] = '#'
    return '\n'.join([''.join(row) for row in a.tolist()])+'\n'
