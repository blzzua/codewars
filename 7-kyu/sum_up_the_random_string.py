# https://www.codewars.com/kata/55da6c52a94744b379000036

import re
def sum_from_string(strng):
    return sum(map(int,re.findall(r'\d+',strng)))


