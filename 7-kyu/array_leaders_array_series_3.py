# https://www.codewars.com/kata/5a651865fd56cb55760000e0

def array_leaders(arr):
    res = []
    while arr:
        t = arr.pop(0)
        if t > sum(arr):
            res.append(t)
    return res


