# https://www.codewars.com/kata/563f879ecbb8fcab31000041

def factory(x):
    def func(arr):
        return [a * x for a in arr]
    return func

