# https://www.codewars.com/kata/605f5d33f38ca800322cb18f

import itertools 
letters = 'abcdefghijlmnopqrstuvwxyz'
cipher = {}
for l,(c1,c2) in zip(letters, itertools.product(range(1,6),range(1,6))):
    cipher[l] = (c1,c2)
    
def tap_code_translation(text):
    return ' '.join(['.' * cnt for cnt in itertools.chain.from_iterable([cipher[letter] for letter in text.replace('k','c').lower()])])

