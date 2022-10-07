# https://www.codewars.com/kata/592edfda5be407b9640000b2

from string import ascii_letters 
from itertools import cycle
def decode(code, key):
    alpha = ' ' + ascii_letters 
    return ''.join(alpha[c-k] for c, k in zip(code, cycle([int(c) for c in str(key)])))

