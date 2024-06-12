# https://www.codewars.com/kata/5a903c0557c562cd7500026f

from itertools import combinations
def solve(arr):
    res = 0
    for c in combinations(arr, 3):
        if c[1] - c[0] == c[2] - c[1]:
            res += 1
    return res

# solution without itertools.combinations:
def solve(arr):
    res = 0
    for i1, v1 in enumerate(arr[:-2]):
        for i2, v2 in enumerate(arr[i1+1:-1]):
            for i3, v3 in enumerate(arr[i2+1:]):
                if v2-v1 == v3-v3:
                    res += 1
    return res              

