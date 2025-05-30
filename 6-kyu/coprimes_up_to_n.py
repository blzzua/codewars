# https://www.codewars.com/kata/59e0dbb72a7acc3610000017

from math import gcd
def coprimes(n):
    res = [1]
    for i in range(2,n):
        if gcd(n, i) == 1:
            res.append(i)
    return res
