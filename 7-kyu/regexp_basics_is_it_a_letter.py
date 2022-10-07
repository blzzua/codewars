# https://www.codewars.com/kata/567de72e8b3621b3c300000b

import re
def is_letter(s):
    print(s)
    return bool(re.fullmatch(r'[a-z]', s, flags=re.I))


