# https://www.codewars.com/kata/55a58505cb237a076100004a

def find_2nd_largest(arr):
    arr = list(set(filter(lambda x: type(x) == int, arr)))
    if len(arr) > 1:
        arr.sort(reverse=True)
        return arr[1]

