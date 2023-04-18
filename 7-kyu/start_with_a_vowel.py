# https://www.codewars.com/kata/5a02e9c19f8e2dbd50000167

import re
from string import ascii_letters, digits

def vowel_start(st): 
    al = ascii_letters + digits
    sl = ''.join(c.lower() for c in st if c in al)
    return re.sub(r'\B([aeiou])', r' \1', sl)
