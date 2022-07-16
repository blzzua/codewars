# https://www.codewars.com/kata/5906436806d25f846400009b
import numpy as np

def x(n):
    a = np.eye(n, dtype=int) | np.fliplr(np.eye(n, dtype=int))
    return '\n'.join([''.join([{0:'□',1:'■'}[c] for c in row]) for row in a.tolist()])
  
  
