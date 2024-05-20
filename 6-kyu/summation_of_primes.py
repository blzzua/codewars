# https://www.codewars.com/kata/59ab0ca4243eae9fec000088

from gmpy2 import next_prime

def summation_of_primes(primes):
    p = next_prime(0)
    res = 0
    while p <= primes:
        res += p
        p = next_prime(p)
    return res
