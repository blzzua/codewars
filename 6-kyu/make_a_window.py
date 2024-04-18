# https://www.codewars.com/kata/59c03f175fb13337df00002e

import numpy as np
def make_a_window(num):
    w = num*2+3
    m = w//2
    a = np.ndarray((w,w),dtype=object)
    a[:] = '.'
    a[0:,m] = '|'
    a[m,:] = '-'
    a[0:,0] = '|'
    a[0:,-1] = '|'
    a[0,:] = '-'
    a[-1,:] = '-'
    a[m,m] = '+'
    return '\n'.join((''.join(line) for line in  a.tolist()))
