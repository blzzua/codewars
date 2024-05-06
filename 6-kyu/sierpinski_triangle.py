# https://www.codewars.com/kata/58add662ea140541a50000f7

import numpy as np 
def sierpinski(n): # ver 1
    if n == 1: return ' * \n* *'
    # base 4x4 triangle
    base_size = 4 
    base = np.ndarray((base_size,base_size), dtype=object)
    base[:] = ' '
    empty = np.copy(base)
    for i in range(base_size):
        base[i, i] = '*'
        base[-1, i] = '*'
        base[i, 0] = '*'

    result = base
    while n > 2: # avoid recursion
        result = np.block([[base, empty], [base, base]])
        base = np.copy(result)
        empty = np.block([[empty, empty], [empty, empty]])
        n = n - 1
    
    linelen = result.shape[0] * 2 - 1 
    res_array = []
    for i, row in enumerate(result):
        offset = result.shape[0] - i -1
        line =  (' ' * offset + ' '.join(row))[:linelen]
        res_array.append(line)
    return '\n'.join(res_array)



def sierpinski(n): # ver 2
    base = np.array('*').reshape((1,1))
    empty = np.array(' ').reshape((1,1))
    for i in range(n): #
        result = np.block([[base, empty], [base, base]])
        base = np.copy(result)
        empty = np.block([[empty, empty], [empty, empty]])
    # inline result formatting:
    return '\n'.join([(' ' * (result.shape[0] - i -1) + ' '.join(row))[:(result.shape[0] * 2 - 1)] for i, row in enumerate(result)])
