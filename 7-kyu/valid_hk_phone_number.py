# https://www.codewars.com/kata/56f54d45af5b1fec4b000cce

import re
def is_valid_HK_phone_number(number):
    return bool(re.match('^\d{4} \d{4}$', number))

def has_valid_HK_phone_number(number):
    print(number)
    return bool(re.findall('\d{4} \d{4}', number))
