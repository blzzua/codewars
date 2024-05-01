# https://www.codewars.com/kata/5653d33e78e3d9dfe600004e

from itertools import product
CODES = {'1': '1', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ', '0': '0'}
def telephone_words(digit_string):
    return [''.join(comb) for comb in product(*[CODES.get(d) for d in digit_string])]
