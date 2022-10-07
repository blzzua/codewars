# https://www.codewars.com/kata/598f76a44f613e0e0b000026

import re
def sum_of_integers_in_string(s):
    return sum(map(int, re.findall(r'\d+', s)))

