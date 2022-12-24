# https://www.codewars.com/kata/554dc2b88fbafd2e95000125

import numpy as np
def vector_length(vector):
    return np.linalg.norm(np.array(vector[0]) - np.array(vector[1]))
