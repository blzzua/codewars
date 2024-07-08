# https://www.codewars.com/kata/5759513c94aba6a30900094d

from math import prod
def sum_prod(strexpression):
    res = 0
    for mult_part in strexpression.split('+'):
        res += prod(map(float, mult_part.split('*')))
    return f'{res:.5e}'
