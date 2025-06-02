# https://www.codewars.com/kata/520b9d2ad5c005041100000f

import re
def pig_it(text):
    return re.sub(r'(\w)(\w*)', r'\2\1ay', text)
