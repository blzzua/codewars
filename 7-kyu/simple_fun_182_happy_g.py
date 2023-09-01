# https://www.codewars.com/kata/58bcd27b7288983803000002

from itertools import groupby
def happy_g(s):
    for g, val_iter in groupby(s):
        if g == 'g' and len(list(val_iter)) == 1:
            return False
    return True
