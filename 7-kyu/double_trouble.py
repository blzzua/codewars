# https://www.codewars.com/kata/57f7796697d62fc93d0001b8

def trouble(x, t):
    res = [x[0]]
    for i in x[1:]:
        if i + res[-1] != t:
            res.append(i)
    return res

