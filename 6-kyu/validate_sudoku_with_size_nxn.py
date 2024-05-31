# https://www.codewars.com/kata/540afbe2dc9f615d5e000425

import numpy as np

class Sudoku(object):
    def __init__(self, data):
        try:
            if any([isinstance(c, bool) for line in data for c in line]):
                raise ValueError('Wrong type') # boolean
            self.a = np.array(data)
            self._invalid = None
        except ValueError:
            self._invalid = True
            
    def is_valid(self):
        if self._invalid:
            return False
        x, y = self.a.shape
        size = int(x**0.5)
        if not(size*size == x == y):
            return False
        numbers = set(range(1,(size*size)+1))
        return all(set(self.a[line, :]) == numbers for line in range(size)) and \
               all(set(self.a[:,col]) == numbers for col in range(size)) and \
               all(set(self.a[y*size+0: y*size+size, x*size+0:x*size+size].ravel()) == numbers 
                              for x,y in np.ndindex((size,size)))

