# https://www.codewars.com/kata/58ad388555bf4c80e800001e

def cut_the_ropes(arr):
    res = [len(arr)]
    for i in arr:
        m = min(arr)
        arr = [x - m for x in arr if x > m]
        rem = len(arr) - arr.count(0)
        if rem == 0:
            return res
        res.append(rem)
