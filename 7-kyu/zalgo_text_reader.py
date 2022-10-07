# https://www.codewars.com/kata/588fe9eaadbbfb44b70001fc

import re
def read_zalgo(zalgotext):
    return ''.join(re.findall(r'[ -z]', zalgotext))

