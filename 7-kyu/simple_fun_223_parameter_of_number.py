# https://www.codewars.com/kata/5902f1839b8e720287000028
from math import gcd, prod

def parameter(n):
    dd = [int(d) for d in str(n)]
    s = sum(dd)
    p = prod(dd)
    lcm = s*p/gcd(s,p)
    return lcm
