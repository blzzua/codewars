# https://www.codewars.com/kata/5a516c2efd56cbd7a8000058

from gmpy2 import is_prime
from itertools import product

single_digit_prime = [2,3,5,7]
total_primes = single_digit_prime[:]
def populate_total_primes():
    
    single_digit_prime_ones = [3, 7] # xx2 and xx5 are not prime, because divisible to 2 and 5
    for fullcomb in range(1,7): 
        for tens, ones in product(product(single_digit_prime,repeat=fullcomb), single_digit_prime_ones):
            d = int(''.join(map(str,tens))) * 10 + ones
            if is_prime(d):
                total_primes.append(d)

populate_total_primes()

def get_total_primes(a, b):
    return sum(1 for i in total_primes if a <= i < b)
