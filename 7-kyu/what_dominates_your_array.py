# https://www.codewars.com/kata/559e10e2e162b69f750000b4

def dominator(arr):
    for i in arr:
        if arr.count(i) > len(arr)/2:
            return i
    return -1

