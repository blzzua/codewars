# https://www.codewars.com/kata/58fd96a59a9f65c2e900008d

from itertools import chain 
def smallest_integer(matrix):
    a = set(i for i in chain.from_iterable(matrix) if i >= 0)
    if a:
        d = set(range(0,max(a) + 2)) - a 
        return min(d)
    else:
        return 0


