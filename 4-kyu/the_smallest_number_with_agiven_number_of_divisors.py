# https://www.codewars.com/kata/638af78312eae9a23c9ec5d6
#    NOT WORKING at 100%, some test when number is factorizing into lot of two's, the algorythm is fails

from gmpy2 import next_prime, is_divisible, isqrt
from itertools import accumulate
from math import prod
from collections import Counter

PRIME_SIZE=10000
primes = list(accumulate(range(PRIME_SIZE), func=lambda x,y: next_prime(x), initial=2))

def f(d:int) -> int:
#    NOT WORKING at 100%
#    fs = [*factors(d)]
#    c = Counter(fs)
#    if c[2] > len(fs) // 2:
#        print(f'two factor {d}' )
#        #return d
    if d in primes: return 2**(d-1)
    dividors = []
    for i, p in enumerate(primes):
        while is_divisible(d,p):
            dividors.append(p)
            d = d // p
    return prod(p ** (d-1) for d,p in zip(dividors[::-1], primes))

# 
def factors(n):
    j = 2
    while n > 1:
        for i in range(j, isqrt(n) + 1):
            if n % i == 0:
                n //= i ; j = i
                yield i
                break
        else:
            if n > 1:
                yield n; break
