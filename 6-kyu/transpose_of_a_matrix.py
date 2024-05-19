# https://www.codewars.com/kata/559656796d8fb52e17000003

def transpose(arr):
    return [list(col) for col in zip(*arr)]
