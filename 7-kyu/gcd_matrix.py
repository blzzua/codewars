# https://www.codewars.com/kata/58a30be22d5b6ca8d9000012

from itertools import product
import numpy as np
def gcd_matrix(a,b):
    ar = np.ndarray((len(a),len(b)), dtype=np.uint64)
    for (i, ai), (j, bj) in product(enumerate(a),enumerate(b)):
        ar[i][j] = np.gcd(ai, bj)
    return round(ar.mean(),3)
    

