# https://www.codewars.com/kata/5a04133e32b8b998dc000089

def solve(arr):
    res = []
    while arr:
        t = arr.pop(0)
        if all(i<t for i in arr):
            res.append(t)
    return res


