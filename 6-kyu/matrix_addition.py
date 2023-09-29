# https://www.codewars.com/kata/526233aefd4764272800036f

import numpy as np
def matrix_addition(*args):
    return sum(map(np.array, args)).tolist()
