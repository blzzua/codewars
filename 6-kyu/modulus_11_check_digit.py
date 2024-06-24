# https://www.codewars.com/kata/568d1ee43ee6afb3ad00001d

from itertools import cycle 
def add_check_digit(number):
    checksum = sum(f * int(d) for f,d in zip(cycle([2,3,4,5,6,7]), number[::-1]))
    remainder = checksum %  11
    if remainder == 0:
        check_symbol = '0'
    elif remainder == 1:
        check_symbol = 'X'
    else:
        check_symbol = str(11-remainder)
    return number + check_symbol
