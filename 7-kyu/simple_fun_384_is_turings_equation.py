# https://www.codewars.com/kata/5a1e6323ffe75f71ae000026

import re
def is_turing_equation(s):
    a,b,c = map(lambda x: int(x[::-1]), re.findall(r'(\d+)',s))
    return a+b == c
