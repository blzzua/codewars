# https://www.codewars.com/kata/564fa92d1639fbefae00009d

from math import gcd
def factors(n):
    if type(n) is int and n > 0:
        return [x for x in range(n,0,-1) if n % x == 0 ]
    else:
        return -1

    






