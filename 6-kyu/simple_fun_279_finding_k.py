# https://www.codewars.com/kata/5919427e5ffc30804900005f

def finding_k(arr):
    return max([m for m in range(max(arr)-1, 0, -1) if len(set(i % m for i in arr)) == 1], default=-1)


def finding_k(arr):
    max_arr = max(arr)
    res = []
    for m in range(max_arr-1, 0, -1):
        if len(set(i % m for i in arr)) == 1:
            res.append(m)
    return max(res, default=-1)

# more math solution than combinations:
from math import gcd
from functools import reduce
def finding_k(arr):
    res = reduce(gcd, [i - arr[0] for i in arr]) 
    if res != 0:
        return res
    else:
        return -1

