# https://www.codewars.com/kata/5436f26c4e3d6c40e5000282

from math import copysign, comb
def sum_of_n(n):
    return [ int(copysign(comb(i,2),n)) for i in range(1,abs(n)+2) ]


