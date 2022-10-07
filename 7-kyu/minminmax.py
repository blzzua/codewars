# https://www.codewars.com/kata/58d3487a643a3f6aa20000ff

def minMinMax(arr):
    a = min(arr)
    b = max(arr)
    res = 0
    for i in range(a, -~b):
        if i not in arr:
            res += i
            break
    return [a, res, b]

