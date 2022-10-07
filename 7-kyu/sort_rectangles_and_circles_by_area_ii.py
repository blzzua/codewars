# https://www.codewars.com/kata/5a1ebc2480171f29cf0000e5

from math import pi, prod
def sq(obj):
    if isinstance(obj,int) or isinstance(obj,float):
        return pi*obj**2
    if isinstance(obj,tuple):
        return prod(obj)
    print(obj)

def sort_by_area(seq): 
    return sorted(seq, key=sq)

