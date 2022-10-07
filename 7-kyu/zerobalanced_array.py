# https://www.codewars.com/kata/59c6fa6972851e8959000067

def is_zero_balanced(arr):
    if sum(arr) != 0 or len(arr) == 0:
        return False
    arr = sorted(arr)
    while len(arr)>1:
        if arr.pop(0) != -arr.pop():
            return False
    return True


