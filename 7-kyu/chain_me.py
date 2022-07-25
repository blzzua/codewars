# https://www.codewars.com/kata/54fb853b2c8785dd5e000957

# trivial
def chain(init_val, functions):
    for f in functions:
        init_val = f(init_val)
    return init_val


# clever:
from functools import reduce
def chain(init_val, functions):
    return reduce(lambda x, f: f(x), functions, init_val)
