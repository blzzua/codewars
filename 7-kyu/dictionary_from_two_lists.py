# https://www.codewars.com/kata/5533c2a50c4fea6832000101

from itertools import zip_longest
def createDict(keys, values):
    return {k:v for k,v in zip_longest(keys, values) if not k is None}

