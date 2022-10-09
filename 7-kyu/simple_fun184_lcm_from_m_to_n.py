# https://www.codewars.com/kata/58bcdc65f6d3b11fce000045

from math import gcd
def mn_lcm(m,n):
    m,n = sorted([m,n])
    res = 1
    for i in range(m,n+1):
        res = res*i//gcd(res,i)
    return res

  

# clever usage reduce + math.lcm
from math import lcm
from functools import reduce
def mn_lcm(m, n):
    m, n = sorted([m, n])
    return reduce(lambda a, b: lcm(a, b), range(m, n+1), 1)
