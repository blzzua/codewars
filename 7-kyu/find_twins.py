# https://www.codewars.com/kata/5834315e06f227a6ac000099

from collections import Counter
def elimination(arr):
    c = Counter(arr)
    try:
        return next(p for p in c if c[p] == 2)
    except StopIteration as e:
        return
