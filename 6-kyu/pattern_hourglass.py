# https://www.codewars.com/kata/56e6d4c466d4428e29000f65

import numpy as np

def draw(n):
    A = np.ndarray( (n+4, n), dtype='object')
    A[:] = '　'    #backgrouund
    A[0,:] = '■'   #top line
    A[-1,:] = '■'  #bottom line
    A[1,:] = '∷'   #top empty
    A[-2,:] = '∷'  #bottom empty
    A[-2,0] = '■'  
    A[-2,-1] = '■' 
    A[1, 0] = '■'  
    A[1, -1] = '■'
    for i in range(n):
        for j in range(i+1, n-i-1):
            A[2+i, j ] = '∷'
            A[n-(2+i)-1+4, j ] = '∷'
        A[2+i, i] = '■'
        A[2+i, n-i-1] = '■'
    return '\n'.join([''.join(c for c in line ) for line in A])    


