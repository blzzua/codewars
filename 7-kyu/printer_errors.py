# https://www.codewars.com/kata/56541980fa08ab47a0000040

import re
def printer_error(s):
    m = re.sub(r'[a-m]', '', s)
    return f'{len(m)}/{len(s)}'

