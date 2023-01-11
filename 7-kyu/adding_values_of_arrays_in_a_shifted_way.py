# https://www.codewars.com/kata/57c7231c484cf9e6ac000090

from itertools import zip_longest

def sum_arrays(arrays, shift):
    result = arrays[0]
    shiftcnt = 0
    for arr in arrays[1:]:
        shiftcnt += 1
        pad = [0,]*(shift*shiftcnt)
        result = [sum(values) for values in zip_longest(result, pad + arr, fillvalue=0)]
    return result
