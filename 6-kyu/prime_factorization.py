# https://www.codewars.com/kata/534a0c100d03ad9772000539

import gmpy2
from collections import defaultdict

class PrimeFactorizer:
    def __init__(self, value):
        self.value = value

    @property
    def factor(self): 
        return self.factorize(self.value)
    
    @staticmethod
    def factorize(n):
        factors = defaultdict(int)
        while n > 1:
            if gmpy2.is_prime(n):
                prime = int(n)
                factors[prime] += 1
            else:
                prime = gmpy2.next_prime(1)
                while n % prime != 0:
                    prime = gmpy2.next_prime(prime)
                factors[int(prime)] += 1
            n //= prime
        return dict(factors)
