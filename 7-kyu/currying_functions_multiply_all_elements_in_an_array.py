# https://www.codewars.com/kata/586909e4c66d18dd1800009b

class multiply_all:
    def __init__(self, arr):
        self._arr = arr
    def __call__(self, n):
        return [i * n for i in self._arr]


