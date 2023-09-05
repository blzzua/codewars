# https://www.codewars.com/kata/5a34da5dee1aae516d00004a

import numpy as np
def get_matrix(n):
    return np.diag(np.full(n,1)).tolist()
