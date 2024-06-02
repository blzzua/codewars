# https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6

# unclear lot of workarounds, solution: but without string<->int convertsion
from itertools import zip_longest, count
def leading_zeroes_workaround(arr):
    res = arr[:]
    for i in range(len(arr)):
        if arr[i] == 0:
            res.pop(0)
        else:
            break
    if res:
        return res
    else:
        return [0]

def sum_arrays(array1,array2):
    if array1 == [] and array2 == []:
        return [] # wtf?
    
    if array1 == []:
        return leading_zeroes_workaround(array2)
    if array2 == []:
        return leading_zeroes_workaround(array1)
    power = 0
    n = 0
    sig1 = 1 if array1[0] >= 0 else -1
    sig2 = 1 if array2[0] >= 0 else -1
    for a,b in zip_longest(array1[::-1],array2[::-1], fillvalue=0):
        n += (10 ** power ) * (abs(a) * sig1 + abs(b) * sig2)
        power += 1
    res = []
    sig = 1 if n >= 0 else -1
    n *= sig
    while n > 0:
        n, digit = divmod(n, 10)
        res.append(digit)
    
    if res:        
        res[-1] *= sig
        res = res[::-1]
        return leading_zeroes_workaround(res)
    else:
        return [0]
