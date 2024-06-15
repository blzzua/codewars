# https://www.codewars.com/kata/58275b63083e128edb00098d

def lucky_sevens(arr):
    res = 0 
    for i, line in enumerate(arr):
        for j, x in enumerate(line):
            if x == 7:
                ssum = 0
                if 0 < i:
                    ssum += arr[i-1][j]
                if i < len(arr) - 1:
                    ssum += arr[i+1][j]
                if 0 < j:
                    ssum += arr[i][j-1]
                if j < len(line) - 1 :
                    ssum += arr[i][j+1]
                if round(ssum**(1/3))**3 == ssum:
                    res += 1
    return res


# scipy.signal  solution
import numpy as np
from scipy import signal
..
a=np.array(a, int)
mask=np.array([[0,1,0],[1,0,1],[0,1,0]])
ssum = signal.convolve2d(a, mask, mode='same')[a==7]
return sum(np.floor(np.cbrt(ssum))**3==ssum)
