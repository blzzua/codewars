# https://www.codewars.com/kata/58f671ee5522a9c33800009b

from functools import reduce

def mult_implication(lst):
    if lst:
        return reduce(lambda x, y: not x or y, lst, True)
