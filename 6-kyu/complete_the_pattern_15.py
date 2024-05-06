# https://www.codewars.com/kata/558db3ca718883bd17000031

import numpy as np
def pattern(n, h=1, v=1, *args):
    if n < 1:
        return ""
    h = max(h,1)
    v = max(v,1)
    a = np.ndarray((2*n-1,2*n-1), dtype=object)
    a[:] = ' '
    for i,val  in enumerate( [*range(1, n)] + [*range(n,0,-1)]):
        a[i,i]= str(val%10)
        a[i,-i-1]= str(val%10)
    horisontal = np.hstack([a] + [a[:,1:]] * (h-1))
    vertical = np.vstack([horisontal] + [horisontal[1:,:]] * (v-1))
    return '\n'.join([''.join(row) for row in vertical.tolist()])
