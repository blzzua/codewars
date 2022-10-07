# https://www.codewars.com/kata/59b844528bcb7735560000a0

def is_nice(arr):
    if not arr:
        return False
    for n in arr:
        if not( n+1 in arr or n-1 in arr):
            return False
    else:
        return True

