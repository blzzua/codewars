# https://www.codewars.com/kata/59e270da7997cba3d3000041

from itertools import groupby
def zero_plentiful(arr):
    res = 0
    print(arr)
    for g, vals in groupby(arr):
        if g == 0:
            if len(list(vals)) >= 4:
                res += 1
            else:
                return 0
    return res
