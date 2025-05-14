# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

def zeros(n):
    if n < 5:
        return 0
    res = 0
    while n > 0:
        n, _ = divmod(n, 5)
        res += n
    return res

# first attempt work_but_too_slow
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

def zeros_work_but_too_slow(n):
    if n < 5:
        return 0
    cnts = Counter()
    for i in range(2,n+1):
        c = Counter(factorize(i))
        cnts = cnts + c
    return min([cnts[2], cnts[5]])
