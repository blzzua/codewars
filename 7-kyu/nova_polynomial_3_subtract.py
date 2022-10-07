# https://www.codewars.com/kata/5714041e8807940ff3001140

from itertools import zip_longest
def poly_subtract(*args):
    return [a - b for a, b in zip_longest(*args, fillvalue=0)]

