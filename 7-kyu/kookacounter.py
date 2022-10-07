# https://www.codewars.com/kata/58e8cad9fd89ea0c6c000258

from itertools import groupby
def kooka_counter(laughing):
    return len(list(groupby(laughing.replace('a',''))))


