# https://www.codewars.com/kata/56e67d6166d442121800074c

import numpy as np
def draw(waves):
    a = np.ndarray(( len(waves),max(waves)),dtype=object)
    a[:] = '□'
    for i, v in enumerate(waves):
        a[i,0:v] = '■'
    a = np.rot90(a)
    return '\n'.join((''.join(line) for line in  a.tolist()))
