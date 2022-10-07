# https://www.codewars.com/kata/5a63948acadebff56f000018

from math import prod
def max_product(lst, n):
    lst.sort(reverse=True)
    return prod(lst[:n])

