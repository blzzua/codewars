# https://www.codewars.com/kata/5bb3e299484fcd5dbb002912

from math import comb
cache = {i: comb(i ,2) for i in range(200)}

def pyramid(balls):
    # too lazy for solve this task.
    for i in range(200):
        if cache[i] > balls:
            break
    return i-2


