# https://www.codewars.com/kata/63b4758f27f8e5000fc1e427

from itertools import groupby
def yahtzee_upper(dice):
    variants =  [d * len(list(data)) for d, data  in groupby(sorted(dice))]
    return max(variants)
