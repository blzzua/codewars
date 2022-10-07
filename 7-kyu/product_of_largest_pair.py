# https://www.codewars.com/kata/5784c89be5553370e000061b

from heapq import nlargest
from math import prod
def max_product(a):
    return prod(nlargest(2,a))

