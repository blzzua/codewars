# https://www.codewars.com/kata/588854201361435f5e0000bd

def array_conversion(arr):
    while True:
        if len(arr) > 1:
            arr = [a + b for a, b in zip(arr[::2], arr[1::2])]
        else:
            break
        if len(arr) > 1:
            arr = [a * b for a, b in zip(arr[::2], arr[1::2])]
        else:
            break
    return arr[0]
