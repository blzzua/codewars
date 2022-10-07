# https://www.codewars.com/kata/56e56756404bb1c950000992

from math import gcd, prod
def sum_differences_between_products_and_LCMs(pairs):
    return sum(prod(pair)-prod(pair)//gcd(*pair) for pair in pairs if prod(pair))

