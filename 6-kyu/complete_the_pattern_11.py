# https://www.codewars.com/kata/5589ad588ee1db3f5e00005a

import numpy as np

def pattern(n):
    sz = 
    a = np.ndarray((n * 3 - 2, n * 3 - 2 ),dtype=object)
    a[n-1:2*n-1, n-1:2*n-1] = str( (n)%10 )
    for i in range(n-1):
        a[0:,i]=str( (i+1)%10 )
        a[0:,-(i+1)]=str( (i+1)%10 )
        a[i,0:]=str( (i+1)%10 )
        a[-(i+1), 0:]=str( (i+1)%10 )

    for i in range(4):
        a[0:n-1, 0:n-1] = ' '
        a = np.rot90(a)
    return '\n'.join((''.join(line) for line in  a.tolist()))
