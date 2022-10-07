# https://www.codewars.com/kata/5ac5e9aa3853da25d9000102

from itertools import zip_longest
def or_arrays(arr1, arr2, fillvalue = 0):
    return [a | b for a,b in zip_longest(arr1, arr2, fillvalue=fillvalue)]

