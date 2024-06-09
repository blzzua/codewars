# https://www.codewars.com/kata/6470e15f4f0b26052c6151cd

import numpy as np
def create_euler_square(n): ## Assume n is odd.
    latin_square1 = np.ones((n,n), dtype=int)
    latin_square2 = np.ones((n,n), dtype=int)
    for i,j in np.ndindex((n,n)):
        latin_square1[j,i] = (j + 2 + i) % n + 1
        latin_square2[j,i] = (j + 2 * i) % n + 1
    return latin_square1.tolist(), latin_square2.tolist()

