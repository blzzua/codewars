# https://www.codewars.com/kata/570ac43a1618ef634000087f

from itertools import zip_longest
def poly_add(*args):
    return [a + b for a, b in zip_longest(*args, fillvalue=0)]

