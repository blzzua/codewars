# https://www.codewars.com/kata/52fba66badcd10859f00097e

import re
def disemvowel(s):
    return re.sub(r'[aeiou]','', s, flags = re.I)

