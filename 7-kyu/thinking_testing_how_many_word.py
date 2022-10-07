# https://www.codewars.com/kata/56eff1e64794404a720002d2

import re
def testit(s):
    return len(re.findall(r'(w.*?o.*?r.*?d)', s, flags = re.I))

