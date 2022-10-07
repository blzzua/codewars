# https://www.codewars.com/kata/53d2697b7152a5e13d000b82

from copy import copy 
def copy_list(l):
    if l is None:
        raise ValueError
    else:
        return copy (l)

