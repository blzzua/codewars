# https://www.codewars.com/kata/5a090c4e697598d0b9000004

def solve(arr):
    res = []
    while len(arr)>1:
        res.append(arr.pop(arr.index(max(arr))))
        res.append(arr.pop(arr.index(min(arr))))
    if arr:
        res = res + arr
    return res


