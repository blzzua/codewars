# https://www.codewars.com/kata/586e1d458cb711f0a800033b

from math import prod
def process_data(data):
    return prod(a-b for a,b in data)

