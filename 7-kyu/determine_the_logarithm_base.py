# https://www.codewars.com/kata/5ae1dcde9c0e489ae00019fc

from math import log10
def determine_base(log_func):
    example_value  = 10000    
    return 10 ** (log10(example_value) / log_func(example_value))

