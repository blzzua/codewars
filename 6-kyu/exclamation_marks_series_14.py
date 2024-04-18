# https://www.codewars.com/kata/57fb1705f815ebd49e00024c/
# Exclamation marks series #14: Convert the exclamation marks and question marks to a prime number

from itertools import groupby
from gmpy2 import is_divisible, next_prime

def convert(s):
    s_nums = [len(list(l)) for _, l in groupby(s)]
    number = sum( m * 10 ** e for m, e in zip(s_nums[::-1], range(len(s))))
    max_prime = 2
    while max_prime < number:
        if is_divisible(number, max_prime):
            number = number // max_prime
        else:
            max_prime = next_prime(max_prime)
    return max_prime
