# https://www.codewars.com/kata/5a905c2157c562994900009d

from math import prod
def product_array(numbers):
    return [prod(numbers)//n for n in numbers]

