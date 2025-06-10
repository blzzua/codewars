# https://www.codewars.com/kata/58b626ee2da07adf3e00009c
# Simple Fun #171: Get Candy Position

def tokenize(a):
    a_dict = dict()
    res = []
    for c in a:
        if c in a_dict:
            res.append(a_dict[c])
        else:
            res.append(num_val:=max(a_dict.values(), default=0) + 1)
            a_dict[c] = num_val
    return res

def isomorph(a, b):
    return tokenize(a) == tokenize(b)
