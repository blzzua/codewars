# https://www.codewars.com/kata/570eb07e127ad107270005fe

import numpy as np
def poly_multiply(*args):
    print(args)
    if all(a for a in args):
        return np.polynomial.polynomial.polymul(*args).tolist()
    else:
        return []
    

