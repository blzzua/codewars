#  https://www.codewars.com/kata/567ed73340895395c100002e

import re
def signed_eight_bit_number(number):
    # grex-generated regex
    return bool(re.match(r'(?:\-(?:1(?:(?:2[0-8]|[3-9])|2?)|(?:1[01]|[2-9])[0-9]?)|1(?:2[0-7]|[3-9])|(?:1[01]|[2-9])[0-9]?|12?|0)\Z', number))
