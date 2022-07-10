# https://www.codewars.com/kata/52774a314c2333f0a7000688

import re
def valid_parentheses(string):
    try:
        re.compile(string)
        return True
    except:
        return False
