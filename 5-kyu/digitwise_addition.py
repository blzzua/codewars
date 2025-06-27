# https://www.codewars.com/kata/663e0eccecb2d0a12da51f84

from collections import Counter
def digitwise_addition(N, K):
    #N= str(N)
    #print(N, K)
    if K > 1000_000:
        return 0
    c = {i: str(N).count(str(i)) for i in range(0,10)}
    for _ in range(K):
        new =  {i: 0 for i in range(0,10)}
        for i, v in c.items():
            if i == 9:
                new[0] += v
                new[1] += v
            else:
                new[i+1] += v
        c = new
    return sum(c.values()) % 1_000_000_007


# nice solution log(K) because of using matrix multiplication method and power reduction (halving):
import numpy as np
mat = np.matrix([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
])

def digitwise_addition(n, k):
    s = str(n)
    v = np.array([s.count(str(d)) for d in range(10)])
    a = np.identity(10, dtype='int64')
    tmp = mat
    while k:
        if k & 1:
            a = (a @ tmp) % (10**9+7)
        tmp = (tmp @ tmp) % (10**9+7)
        k >>= 1
    return (a @ v).sum() % (10**9+7)
