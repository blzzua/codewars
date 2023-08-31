# https://www.codewars.com/kata/58311faba317216aad000168

from math import log10, ceil
def print_nums(*args):
    m = max(args,default=1)
    ml = ceil(log10(m))
    return '\n'.join(str(i).zfill(ml) for i in args)
