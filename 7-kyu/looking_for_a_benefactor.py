# https://www.codewars.com/kata/569b5cec755dd3534d00000f

from math import ceil, sqrt
def new_avg(arr, newavg):
    e = newavg * float(len(arr) + 1) - sum(arr)
    return ceil(e) + sqrt(e) - sqrt(e) # sqrt raise error

