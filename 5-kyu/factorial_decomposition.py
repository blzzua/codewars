# https://www.codewars.com/kata/5a045fee46d843effa000070

from collections import Counter
from functools import lru_cache
UPPER_LIMIT = 5000

def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    return [i for i in sieve if i]

# global precomputed  primes
primes = eratosthenes(UPPER_LIMIT)

@lru_cache(maxsize=UPPER_LIMIT)
def factorize(n):
    res = []
    while n > 1:
        for i in primes:
            if n % i == 0:
                res.append(i)
                n = n // i
    return res

def decomp(n):
    print(n)
    res  = Counter()
    for k in range(2,n+1):
        res = res + Counter(factorize(k))
    return ' * '.join([ f'{k}' + f'^{res[k]}' if res[k] > 1 else f'{k}' for k in sorted(list(res)) ])


