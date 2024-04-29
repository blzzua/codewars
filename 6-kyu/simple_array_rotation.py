# https://www.codewars.com/kata/5a16cab2c9fc0e09ce000097

import numpy as np

def solve(a):
    def direction(a, s = ''):
        if np.all(np.diff(a) > 0):
            return s+'A'
        elif np.all(np.diff(a) < 0):
            return s+'D'
    a = np.array(a)
    if res:=direction(a, s = ''):
        return res
    for i in range(np.size(a)):
        a = np.roll(a,1)
        if res:=direction(a, s = 'R'):
            return res
