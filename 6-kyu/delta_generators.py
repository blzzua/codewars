# https://www.codewars.com/kata/6040b781e50db7000ab35125

def gen_diff(values):
    g = iter(values)
    b = next(g)
    while True:
        try:
            a = next(g)
            yield a - b 
            b = a 
        except StopIteration:
            return None

def delta(values, n):
    if n == 1:
        return gen_diff(values)
    else:
        return delta(gen_diff(values), n-1)
