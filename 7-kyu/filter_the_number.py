# https://www.codewars.com/kata/55b051fac50a3292a9000025

import re
def filter_string(string):
    return int(''.join(re.findall(r'\d', string)))


