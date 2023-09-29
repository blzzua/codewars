# https://www.codewars.com/kata/5849169a6512c5964000016e

from math import prod
from collections import Counter
from functools import reduce
import gmpy2 

def factorize(n):
    factors = []
    while n > 1:
        prime = gmpy2.next_prime(1)
        while n % prime != 0:
            prime = gmpy2.next_prime(prime)
        factors.append(int(prime))
        n //= prime
    return factors

def intersect(a,b):
    doubled = (Counter(a) + Counter(b)) - (Counter(a) - Counter(b)) - (Counter(b) - Counter(a))
    return list(Counter({k: v//2 for k,v in doubled.items()}).elements())

def greatest_common_factor(seq):
    gcf = reduce(lambda x, y: intersect(x, factorize(y)), seq, factorize(seq[0]))
    return prod(gcf)
