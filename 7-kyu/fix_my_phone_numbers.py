# https://www.codewars.com/kata/596343a24489a8b2a00000a2

import re
def is_it_a_num(s: str) -> str:
    ss = re.sub(r'[^\d]','',s)
    if ss.startswith('0') and len(ss) == 11:
        return ss
    else:
        return 'Not a phone number'

