# https://www.codewars.com/kata/559e708e72d342b0c900007b

from operator import add, mul

def even_odd(arr):
    ret = 0
    for i, val in enumerate(arr):
        op = mul if i % 2 else add
        ret = op(val, ret)
    return ret
