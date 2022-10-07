# https://www.codewars.com/kata/592e830e043b99888600002d

from string import ascii_lowercase
from itertools import cycle
def encode(message, key):
    alpha = ' '+ascii_lowercase
    return ([ alpha.index(m) + int(k)  for m, k in  zip(message, cycle(str(key)))] )
    
    
    

