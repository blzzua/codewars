# https://www.codewars.com/kata/59a9919107157a45220000e1

def find_all(array, n):
    return [i for i, c in enumerate(array) if c == n]
