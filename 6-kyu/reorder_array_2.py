# https://www.codewars.com/kata/5a48fab7bdb9b5b3690009b6

import numpy as np
def reorder(n, m):
    a = np.array(range(n)).reshape((2,n//2))
    for i, c in enumerate(a):
        a[i,:] = np.roll(c,m)
    return a.tolist()
