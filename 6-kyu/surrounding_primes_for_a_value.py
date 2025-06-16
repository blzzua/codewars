# https://www.codewars.com/kata/560b8d7106ede725dd0000e2

from gmpy2 import next_prime
def prime_bef_aft(num):
    prev = p = max([num - 1000, int(num**0.5)] )
    res = []
    while p < num:
        p = next_prime(p)
        if p == num:
            res = [prev, next_prime(p)]
        else:
            res = [prev, p]
        prev = p
    return res
