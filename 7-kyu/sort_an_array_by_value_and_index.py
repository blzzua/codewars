# https://www.codewars.com/kata/58e0cb3634a3027180000040

from numpy import prod
def sort_by_value_and_index(arr):
    return [b for a, b in sorted(enumerate(arr, 1), key=prod)]

