# https://www.codewars.com/kata/56cafdabc8cfcc3ad4000a2b

# this solution does not fit time budget
from functools import reduce
def score(n):
    return reduce(lambda a,b: a|b, range(n+1))


# math solution
from math import log, ceil
def score(n):
    if n:
        return 2**ceil(log(n+1,2))-1
    else: 
        return n

# clever solution 
def score(n):
  return 2**n.bit_length()-1
