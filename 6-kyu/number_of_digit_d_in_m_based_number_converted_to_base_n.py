# https://www.codewars.com/kata/57c18a16c82ce75f4b000020

al = '0123456789abcdefghijklmnopqrstuvwxyz'

def from_dec_to_base(n, to_base):
    res = ''
    while n > 0:
        n, rem = divmod(n, to_base)
        res = al[rem] + res
    return res or '0'

def from_base_to_dec(n_str, from_base):
    res = 0
    for i, d in enumerate(n_str[::-1]):
        res += al.index(d) * (from_base ** i)
    return res

def count_digit(number, digit, base=10, from_base=10):
    res = from_dec_to_base(from_base_to_dec(number, from_base), base)
    return res.count(str(digit))



# clever using libraries:
from numpy import base_repr
base_repr(int(number, from_base), base)

from gmpy2 import mpz
mpz(number, base=from_base).digits(base)
