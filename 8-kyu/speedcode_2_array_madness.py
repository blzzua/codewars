# https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1

import numpy as np
def array_madness(a,b):
    return np.sum(np.square(a)) >= np.sum( np.array(b)**3  )

