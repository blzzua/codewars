# https://www.codewars.com/kata/57096af70dad013aa200007b

from operator import (
    and_ as AND, 
    or_ as OR,
    xor as XOR
    )
from functools import reduce

def logical_calc(array, op):
    return reduce(globals().get(op), array)


