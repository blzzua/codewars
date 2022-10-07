# https://www.codewars.com/kata/55f9064161541a9e01000001

import re
def valid_number(n):
    return bool(re.match(r'^(\+|-)?\d*\.\d{2}$', n))

