# https://www.codewars.com/kata/589ace5eeef39faf49000061

import re
def reverse_parentheses(st):
    while match_list := re.findall(r'\((\w+)\)', st):
        for m in match_list:
            st = st.replace('('+m+')', m[::-1])
    return st


