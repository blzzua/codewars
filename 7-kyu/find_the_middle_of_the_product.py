# https://www.codewars.com/kata/5ac54bcbb925d9b437000001

# lazy ugly probability-success solution
import re
from math import prod, ceil, log10
def find_middle(string):
    try:
        digits = [*map(int, re.findall(r'\d', string))]
        # workarounds
        if digits:
            number = prod(digits)
        else:
            return -1
        if number == 0:
            return 0

        len_number = ceil(log10(abs(number)))
        h1 = len_number//2 
        h2 = h1 - (len_number % 2 ==0)
        return int(str(number)[h2:h1+1])
    except (TypeError) as e:
        return -1
