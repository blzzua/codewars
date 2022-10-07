# https://www.codewars.com/kata/560fbc2d636966b21e00009e

def func(n):
    return int(n) % 2 == 0

def map(arr, somefunction):
    if not callable(somefunction):
        return 'given argument is not a function'
    try:
        [int(num) for num in arr]
    except:
        return 'array should contain only numbers'
    return [somefunction(n) for n in arr]


