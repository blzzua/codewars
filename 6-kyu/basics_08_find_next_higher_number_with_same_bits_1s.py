# https://www.codewars.com/kata/56bdd0aec5dc03d7780010a5

import re
def next_higher(n):
    return int(re.sub(r'0?1(1*)(0*)$', r'10\2\1', bin(n)),2)
