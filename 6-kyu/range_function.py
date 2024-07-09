# https://www.codewars.com/kata/584ebd7a044a1520f20000d5

def range_function(a,b=None,c=None):
    if b is None:
        a, b, c = 1, a, 1
    elif c is None:
        c = 1
    else:
        a, b, c = a, c, b
    value = a
    while value <= b:
        yield value
        value += c
