# https://www.codewars.com/kata/582c01ad3fd1cc5736000348

import numpy as np
def make_matrix(m: int, n: int) -> str:
    a = np.ndarray((n,n),dtype=object)
    s = str(m)
    for i in range(n):
        a[i,i] = s[0]
        a[i,n-i-1] = s[0]
    for val in 1,-1,2,3:
        for i in range(n//2):
            a[i][i+1:n-(i+1)] = s[val]
        a = np.rot90(a)
    return '\n'.join((' '.join(line) for line in  a.tolist()))
