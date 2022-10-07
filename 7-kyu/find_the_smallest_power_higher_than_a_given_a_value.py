# https://www.codewars.com/kata/56ba65c6a15703ac7e002075

from math import ceil
def find_next_power(val, pow_):
    return ceil(val ** (1 / pow_)) ** pow_

