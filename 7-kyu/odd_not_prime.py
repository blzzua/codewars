# https://www.codewars.com/kata/5a9996fa8e503f2b4a002e7a

import gmpy2
N = 10000
i = 1
primes = []
while i < N:
    i = gmpy2.next_prime(i)
    primes.append(i)
odds_not_prime = [i for i in range(1,N,2) if i not in primes]

def odd_not_prime(n):
    return sum(1 for i in odds_not_prime if i <= n)
