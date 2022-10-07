# https://www.codewars.com/kata/58811e9cfd05cb5aed0000a4

import numpy as np
def centroid(c):
    return np.round(np.mean(np.array(c), 0),2).tolist()

