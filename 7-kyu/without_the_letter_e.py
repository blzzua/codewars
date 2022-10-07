# https://www.codewars.com/kata/594b8e182fa0a0d7fc000875

import re
def find_e(s):
    if not s:
        return s
    elif isinstance(s,str):
        res = len(re.findall(r'e',s,flags=re.I))
        if res:
            return str(res)
        else:
            return 'There is no "e".'


