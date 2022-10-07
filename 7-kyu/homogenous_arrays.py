# https://www.codewars.com/kata/57ef016a7b45ef647a00002d

def filter_homogenous(arrays):
    return [arr for arr in arrays if arr and all(type(a) == type(b) for a, b in zip(arr, arr[1:]))]

