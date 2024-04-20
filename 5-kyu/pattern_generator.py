# https://www.codewars.com/kata/598ab728062fc49a22000410

import numpy as np
def pattern_generator(n):
    sz = n * 2 - 1
    if sz < 1:
        return ''
    a = np.ndarray((sz,sz),dtype=object)
    a[:] = ' '
    for t in 0,1:
        for i in range(0,n,2):
            for j in range(i,n):
                a[j, n-1+j-i] = 'o' if i // 2 % 2 else 'x'
        a = a.T
    return '\n'.join((''.join(line) for line in  a.tolist()))
