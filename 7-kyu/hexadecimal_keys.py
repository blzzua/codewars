# https://www.codewars.com/kata/5962ddfc2f9addd52200001d

import gmpy2
def find_key(encryption_key):
    n = int(encryption_key, 16)
    p = 2
    while p < n**0.5:
        p = gmpy2.next_prime(p)
        if n % p == 0:
            return (p - 1 ) * ( n // p - 1 )

