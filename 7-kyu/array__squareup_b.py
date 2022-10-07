# https://www.codewars.com/kata/5a8bcd980025e99381000099

def square_up(n):
    res = []
    for i in range(1, n + 1):
        res.extend([0] * (n - i))
        res.extend([*range(i, 0,  -1)])
    return res

