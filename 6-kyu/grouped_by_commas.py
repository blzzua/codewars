# https://www.codewars.com/kata/5274e122fc75c0943d000148

from itertools import islice

def by3(iterable):
    it = iter(iterable)
    while batch := tuple(islice(it, 3)):
        yield batch

def group_by_commas(n):
    digits = []
    while n:
        n, rem =divmod(n, 10)
        digits.append(rem)
    return ','.join(''.join(map(str,group)) for group in by3(digits))[::-1]
