# https://www.codewars.com/kata/58552bdb68b034a1a80001fb

from math import ceil
def cook_pancakes(n, m):
    return  max(2,ceil(2 * n / m))
