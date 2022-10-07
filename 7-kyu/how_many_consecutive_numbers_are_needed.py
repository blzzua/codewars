# https://www.codewars.com/kata/559cc2d2b802a5c94700000c

def consecutive(arr):
    if arr:
        return len(range(max(arr)-min(arr)+1)) - len(arr)
    else:
        return 0

