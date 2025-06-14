# https://www.codewars.com/kata/55491e9e50f2fc92f3000074

from string import ascii_uppercase 
from math import prod

def ride(group, comet):
    al = ' ' + ascii_uppercase
    c_index = prod(map(al.index, comet)) % 47 
    g_index = prod(map(al.index, group)) % 47
    return ('STAY', 'GO')[c_index == g_index]
