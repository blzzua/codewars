# https://www.codewars.com/kata/52249faee9abb9cefa0001ee

from itertools import groupby
def uniq(seq): 
    return [g for g,v in groupby(seq)]
