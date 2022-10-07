# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0

from string import ascii_lowercase

def solve(arr):
    alphabet = { c:i for i, c in enumerate(ascii_lowercase, 1) }
    return [ sum([ 1 for letter, pos in zip(c, range(len(c))) if alphabet[letter.lower()] == (pos+1) ]) for c in arr]

