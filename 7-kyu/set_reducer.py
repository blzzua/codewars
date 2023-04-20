# https://www.codewars.com/kata/63cbe409959401003e09978b

def reduce(inp):
    res = [1]
    for a,b in zip(inp, inp[1:]):
        if a!=b:
            res.append(1)
        else:
            res[-1] += 1
    return res[:]

def set_reducer(inp):
    while len(inp) > 1:
        res = reduce(inp)
        inp = res[:]
    return res[0]
