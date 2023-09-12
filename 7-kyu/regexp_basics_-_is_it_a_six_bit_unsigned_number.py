# https://www.codewars.com/kata/567e8dbb9b6f4da558000030

import re
def six_bit_number(n):
    return bool(re.match(r'([1-5]?[0-9]|6[0-3])\Z',n))
