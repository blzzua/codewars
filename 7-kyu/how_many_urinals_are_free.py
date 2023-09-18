# https://www.codewars.com/kata/5e2733f0e7432a000fb5ecc4

import re 
from itertools import groupby
def get_free_urinals(urinals):
    if '11' in urinals:
        return -1
    return sum((len(list(g))+1)//2 for c, g in groupby(re.sub(r'(0?10?)','.',urinals)) if c == '0')
