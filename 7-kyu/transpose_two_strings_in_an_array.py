# https://www.codewars.com/kata/581f4ac139dc423f04000b99

from itertools import zip_longest
def transpose_two_strings(arr):
    return '\n'.join(' '.join(letters) for letters in zip_longest(*arr, fillvalue=' '))

