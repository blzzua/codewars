# https://www.codewars.com/kata/59a818191c55c44f3900053f

from math import log10
def true_binary(n):
    a = (n>>1)
    l = a.bit_length()
    bitmask = ((1<<l)^a)
    return [1 if bit == '1' else -1 for bit in bin(bitmask)[2:]]
