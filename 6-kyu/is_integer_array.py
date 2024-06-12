# https://www.codewars.com/kata/52a112d9488f506ae7000b95

def is_int_array(arr):
    if not isinstance(arr, list):
        return False
    for i in arr:
        if not isinstance(i, (int, float)) or i != int(i):
            return False
    return True
