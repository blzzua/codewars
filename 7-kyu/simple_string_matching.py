# https://www.codewars.com/kata/5bc052f93f43de7054000188

import re
def solve(a,b):
    a = a.replace('*','[\w]*')
    return bool(re.fullmatch(a,b))

