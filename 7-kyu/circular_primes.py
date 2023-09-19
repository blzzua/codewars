# https://www.codewars.com/kata/56b2333e2542c2aadb000079

from gmpy2 import is_prime
def circular_prime(n):
    l = len(str(n))
    for i in range(l):
        if is_prime(n):
            a,b = divmod(n, 10 ** (l-1))
            n = b * 10 + a
        else:
            return False
    return True
