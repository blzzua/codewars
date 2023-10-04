# https://www.codewars.com/kata/577c2d68311a24132a0002a5

from itertools import groupby
def reverse(st):
    res = []
    for letter, letter_gen in groupby(st):
        letter_len = len(list(letter_gen))
        if letter_len >= 2:
            letter = letter.swapcase()
        res.append(letter * letter_len)
    return ''.join(res)
