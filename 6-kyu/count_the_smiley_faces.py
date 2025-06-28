# https://www.codewars.com/kata/583203e6eb35d7980400002a

import re
def count_smileys(arr):
    res = 0
    for face in arr:
        if re.fullmatch(r'[:;][-~]?[)D]', face):
            res += 1
            
    return res
    
