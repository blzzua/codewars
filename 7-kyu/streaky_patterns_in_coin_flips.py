# https://www.codewars.com/kata/5c1ac4f002c59c725900003f

from itertools import groupby
def check_sequence(sequence, l, n):
    return sum(1 for  side, g in groupby(sequence) if len([*g]) == l) == n
