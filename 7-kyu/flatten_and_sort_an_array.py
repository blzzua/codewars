# https://www.codewars.com/kata/57ee99a16c8df7b02d00045f

from itertools import chain
def flatten_and_sort(array):
    return sorted(chain(*array))


