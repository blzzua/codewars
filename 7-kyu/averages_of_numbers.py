# https://www.codewars.com/kata/57d2807295497e652b000139

def averages(arr):
    if type(arr) == list and len(arr) > 1:
        return [(a+b)/2 for a,b in zip(arr, arr[1:])]
    else: 
        return []

