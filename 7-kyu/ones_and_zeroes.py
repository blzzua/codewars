# https://www.codewars.com/kata/650a86e8404241005fc744ca

from itertools import groupby
def same_length(txt):
    ones_len = 0
    for d, dgen in groupby(txt):
        if d == '1':
            ones_len = len(list(dgen))
        else:
            if ones_len != len(list(dgen)):
                return False
    return d == '0'
  
