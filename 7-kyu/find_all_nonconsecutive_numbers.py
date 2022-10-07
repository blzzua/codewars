# https://www.codewars.com/kata/58f8b35fda19c0c79400020f

def all_non_consecutive(arr):
    return [{'i': i, 'n': b} for i, (a, b) in enumerate(zip(arr, arr[1:]),1) if b - a != 1]


