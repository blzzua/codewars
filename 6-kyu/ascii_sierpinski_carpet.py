# https://www.codewars.com/kata/630006e1b4e54c7a7e943679

import numpy as np
def sub_carpet(a, dim):
    n = a.shape[0]
    inc = 0
    subdim = 3**(dim-1)
    if dim == 1:
        return np.array((['██','██','██'],['██','  ','██'],['██','██','██']))
    for i in range(3):
        for j in range(3):
            inc = inc+1
            if i == j == 1:
                a[i*subdim:subdim*(i+1),subdim*j:subdim*(j+1)] = '  '
            else:
                sub_a = sub_carpet(a[i*subdim:subdim*(i+1),subdim*j:subdim*(j+1)], dim - 1)
                a[i*subdim:subdim*(i+1),subdim*j:subdim*(j+1)] = sub_a
    return a

def sierpinski_carpet_string(n):
    if n == 0:
        return '██'
    dim = n
    n = 3**dim
    a = np.zeros((n,n), dtype=object)
    res = sub_carpet(a, dim)
    return '\n'.join([''.join(line) for line in res.tolist()])
