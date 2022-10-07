# https://www.codewars.com/kata/5c942f40bc4575001a3ea7ec

from math import prod
def per(n):
    res = []
    while not 0 <= n < 10:
        n = prod(int(i) for i in str(n))
        res.append(n)
    return res

