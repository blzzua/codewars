# https://www.codewars.com/kata/63b84f54693cb10065687ae5

import numpy as np
def create_box(m, n):
    a= np.ones( (n,m), dtype=int)
    for d in range(1, min(a.shape)//2+1):
        for i in range(d, a.shape[0]-d):
            for j in range(d, a.shape[1]-d):
                a[i,j]+=1
    return a.tolist()
