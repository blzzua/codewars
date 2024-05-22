# https://www.codewars.com/kata/5714eb80e1bf814e53000c06

from functools import reduce
def fish_hex(name):
    return reduce(lambda res, letter: res ^ int(letter, 16), filter(lambda x: x in 'abcdef', name.lower()), 0 )

