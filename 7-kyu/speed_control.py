# https://www.codewars.com/kata/56484848ba95170a8000004d

from math import floor
from itertools import pairwise
def gps(s, x):
    if len(x) > 2:
        return floor(max((3600 * (b-a))/s for a,b in pairwise(x)))
    else:
        return 0

