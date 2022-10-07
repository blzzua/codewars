# https://www.codewars.com/kata/56ec1e8492446a415e000b63

from itertools import groupby
def ones_counter(inp):
    return [sum(l) for i, l in groupby(inp) if i>0]

