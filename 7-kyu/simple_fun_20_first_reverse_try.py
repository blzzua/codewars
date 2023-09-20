# https://www.codewars.com/kata/5886c6b2f3b6ae33dd0000be

def first_reverse_try(arr):
    if arr:
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr
