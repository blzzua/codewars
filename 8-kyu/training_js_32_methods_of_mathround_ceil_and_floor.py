# https://www.codewars.com/kata/5732d3c9791aafb0e4001236

from math import floor, ceil

def round_it(n):
    a, b = [len(x) for x in str(n).split('.')]
    if a<b:
        return ceil(n)
    elif a>b:
        return floor(n)
    else:
        return round(n)
    

