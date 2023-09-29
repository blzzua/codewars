# https://www.codewars.com/kata/57f8ff867a28db569e000c4a

import re 
def kebabize(st):
    st2 = re.sub('\d','', st)
    return '-'.join(map(str.lower, re.findall(r'([A-Z]?(?:[a-z]+)|[A-Z])', st2)))
