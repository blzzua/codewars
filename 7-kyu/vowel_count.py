# https://www.codewars.com/kata/54ff3102c1bad923760001f3

import re
def get_count(sentence):
    return len(re.findall(r'[aeiou]', sentence))

