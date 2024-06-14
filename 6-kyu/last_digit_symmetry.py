# https://www.codewars.com/kata/59a9466f589d2af4c50001d8

from gmpy2 import next_prime
import bisect

def precalc():
    n = 2
    primes = []
    while n < 100:
        primes.append(n)
        n=int(next_prime(n))

    return [i for i in range(1000, 1000_000)
        if str(i)[-2:] == str(i*i)[-2:] and ((int(str(i)[:2]) in primes) and (int(str(i*i)[:2]) in primes))]

lds_numbers = sorted(precalc())

def solve(a, b):
    return bisect.bisect_right(lds_numbers, b) - bisect.bisect_left(lds_numbers, a)


# optimizations from JuanCampillo solution:
# After submiting my solution, I have realized that I can further specify the function last_two_digits_ok
# So: x^2= (a+b)^2 = a^2 + b^2 + 2ab
# Example: 421*2 = (400 + 21)^2 = 400^2 + 21^2 + 2*400*21 = 160000 + 441 + 16800 = 177241
# If we separate the last two digits of a number 'x' like that 'a+b', we will have a number (a)
# multiple of 100 and its square (a^2) will also be.
# We will also have the product of this number, two, and the last two digits (2ab), and again,
# being 'a' a multiple of 100, the result of the multiplication will also be a multiple of 100.
# This leaves only the square of the last two digits (b^2) as being responsible for defining the last two digits of (x^2).
# Taking this into account, if we look at all the squares of two-digit numbers that end in 1 or 6
# (01, 11, 21... or 06, 16, 26, ...) we will observe that it is only true in these two cases:
#   01^2 = 01
#   76^2 = 5776
# instead of: str(i)[-2:] == str(i*i)[-2:]
str(i)[-2:] in ['01', '76', '00', '25']

