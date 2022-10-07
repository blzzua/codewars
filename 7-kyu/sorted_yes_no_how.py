# https://www.codewars.com/kata/580a4734d6df748060000045

from math import copysign
def is_sorted_and_how(arr):
    return { 1: 'yes, ascending', -1: 'yes, descending'}.\
            get(sum([copysign(1,b-a) for a,b in zip(arr, arr[1:])])/(len(arr)-1), 'no')

