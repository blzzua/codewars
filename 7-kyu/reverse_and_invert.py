# https://www.codewars.com/kata/5899e054aa1498da6b0000cc

def reverse_invert(lst):
    return [-int(str(i)[::-1]) if i >= 0 else int(str(abs(i))[::-1]) for i in lst if isinstance(i, int)]
