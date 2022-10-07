# https://www.codewars.com/kata/5aa3af22ba1bb5209f000037

import re
def solve(eq):
    return ''.join(re.split(r'([*+-/])',eq)[::-1])

