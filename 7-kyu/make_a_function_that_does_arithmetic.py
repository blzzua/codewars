# https://www.codewars.com/kata/583f158ea20cfcbeb400000a

from operator import (
    add,
    sub as subtract,
    mul as multiply,
    truediv as divide 
    )
from functools import reduce
def arithmetic(a, b, operator):
    return reduce(globals().get(operator),(a,b))


