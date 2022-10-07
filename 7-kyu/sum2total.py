# https://www.codewars.com/kata/559fed8454b12433ff0000a2

from itertools import pairwise
def total(arr):
    if len(arr)>1:
        return total([a+b for a,b in pairwise(arr)])
    else:
        return arr[0]
    

