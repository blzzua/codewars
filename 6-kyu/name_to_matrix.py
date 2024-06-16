# https://www.codewars.com/kata/5a91e0793e9156ccb0003f6e

from math import sqrt, ceil
def matrixfy(st):
    orig_len = len(st)
    if orig_len == 0:
        return 'name must be at least one letter'
    res_len = ceil(sqrt(orig_len))
    pad_len = (res_len*res_len) - orig_len
    if pad_len > 0:
        st = st + '.' * pad_len
    return list(list(row) for row in zip(*[iter(st)] * res_len))


