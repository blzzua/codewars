# https://www.codewars.com/kata/59ec2d112332430ce9000005

import gmpy2 
def factorize(n):
    factors = set()
    while n > 1:
        prime = gmpy2.next_prime(1)
        while n % prime != 0:
            prime = gmpy2.next_prime(prime)
        factors.add(int(prime))
        n //= prime
    return factors

def solve(a,b):
    return all(a % f == 0 for f in factorize(b))


# clever math
while 1 < gmpy2.gcd(a, b):
    b = b // gmpy2.gcd(a, b)
return b == 1
