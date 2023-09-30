# https://www.codewars.com/kata/517abf86da9663f1d2000003

import re
def to_camel_case(text):
    if not text:
        return text
    words = re.findall(r'([A-Za-z]+)',text)
    res = [words.pop(0)]
    res += list(map(str.capitalize, words))
    return ''.join(res)
