# https://www.codewars.com/kata/58c20c8d61aefc518f0000fd

from itertools import groupby
def sum_of_regular_numbers(arr):
    groups = [list(data) for g, data in groupby(zip(arr,arr[1:]) , lambda x: x[1]- x[0])]
    res = 0
    for lst in groups:
        if len(lst) == 1:
            continue
        res += sum([b + a*int(1-bool(i)) for i, (a,b) in enumerate(lst)])
    return res
