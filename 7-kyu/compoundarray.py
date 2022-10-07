# https://www.codewars.com/kata/56044de2aa75e28875000017

from itertools import zip_longest
def compound_array(*args):
    res = []
    for a,b in zip_longest(*args):
        if a is not None:
            res.append(a)
        if b is not None:
            res.append(b)
    return res

