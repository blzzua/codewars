# https://www.codewars.com/kata/57061b6fcb7293901a000ac7

import re
def head_smash(arr):
    if not arr:
        return 'Gym is empty'
    if isinstance(arr, int):
        return "This isn't the gym!!"
    return [re.sub('O',' ', l) for l in arr]

