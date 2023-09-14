# https://www.codewars.com/kata/5ab7ee556a176b1043000047

from math import ceil
def pay_cheese(arr):
    hours = ceil(sum(i / 100 for i in arr)) * 8.75 * 4
    return f'L{hours:.0f}'
