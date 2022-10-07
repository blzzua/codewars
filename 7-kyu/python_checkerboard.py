# https://www.codewars.com/kata/57785441311a24465e000025

import numpy as np
def make_checkered_board(n):
    m = n + (1 - n % 2) 
    a = np.vectorize(lambda i: 'O' if i % 2 else 'X')(np.arange(n*m)).reshape((n,m))
    if n % 2 == 0:
        a = np.delete(a, n ,axis=1)
    return a.tolist()


