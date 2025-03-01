# https://www.codewars.com/kata/58afab67a9c97af7e8000071

import gmpy2
from collections import Counter

def factorize(n):
    factors = []
    while n > 1:
        prime = gmpy2.next_prime(1)
        while n % prime != 0:
            prime = gmpy2.next_prime(prime)
        factors.append(int(prime))
        n //= prime
    return factors


def mul_power(n, k):
    factors = Counter(factorize(n))
    res = 1
    for f, cnt in factors.items():
        if (cnt % k) > 0:
            mult = f **  (k-(cnt % k))
            res *= mult
            print(res, mult, f, cnt, )
    return res
