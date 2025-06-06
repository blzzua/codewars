# https://www.codewars.com/kata/513fa1d75e4297ba38000003

def flatten(*args):
    res = []
    for val in args:
        if isinstance(val, list):
            res.extend(flatten(*val))
        else:
            res.append(val)
    return res
            
