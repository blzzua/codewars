# https://www.codewars.com/kata/584e8bba044a15d3ed00016c

import numpy as np
def mobile_display(n,p):
    n = max(20, n)
    p = max(30, p)
    m = int(n * p / 100)
    a = np.ndarray((m,n), dtype=object)
    a[:] = ' '
    for i,j in np.ndindex(a.shape):
        if i*j == 0 or i == m-1 or j == n-1:
            a[i,j] = '*'
    a[m - 2, 2:2 + len('Menu')] = list('Menu')
    a[m - 2, -(2 + len('Contacts')):-2] = list('Contacts')
    CodeWars_line = 'CodeWars'.center(n-2)
    if n%2:  # looks like str.center() works unproperly
        CodeWars_line = CodeWars_line[1:] + ' '
    logo_line = m//2-1
    a[logo_line, 1:1+len(CodeWars_line)] = list(CodeWars_line)
    return '\n'.join([''.join(row) for row in a.tolist()])
