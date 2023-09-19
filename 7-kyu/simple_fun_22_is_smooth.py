# https://www.codewars.com/kata/5886d35d4703f125a6000008

def is_smooth(arr):
    m, d  = divmod(len(arr), 2)
    middle = sum(arr[m-(1-d):m+1])
    return arr[0] == middle == arr[-1]
