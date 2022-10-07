# https://www.codewars.com/kata/5458d4d2cbae2a9438000389

def make_lazy(op, *args):
    return lambda: op(*args)


