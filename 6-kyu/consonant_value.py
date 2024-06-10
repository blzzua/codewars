# https://www.codewars.com/kata/59c633e7dcc4053512000073

import string
import re
al =  ' ' + string.ascii_lowercase

def word_value(w):
    return sum(map(al.index, w))

def solve(s):
    return max(map(word_value, re.split('[aeiou]', s)))

