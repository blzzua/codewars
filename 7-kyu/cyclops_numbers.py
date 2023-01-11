# https://www.codewars.com/kata/56b0bc0826814364a800005a

from math import log2, ceil
def cyclops (n):
    nb = ceil(log2(n))
    return (nb % 2) * n == (((1<<nb)-1) - (1<<((nb//2))))
