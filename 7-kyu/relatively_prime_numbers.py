# https://www.codewars.com/kata/56b0f5f84de0afafce00004e

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

def relatively_prime (n, l):
    return [i for i in l if not set(factorize(n)).intersection(factorize(i))]

#  return [x for x in l if math.gcd(n, x) == 1]
