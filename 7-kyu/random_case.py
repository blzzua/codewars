# https://www.codewars.com/kata/57073869924f34185100036d

from random import sample
def random_case(x):
    randoms = sample([0,1] * len(x), len(x))
    cases = [str.upper, str.lower]
    return ''.join(cases[r](c) for c, r in zip(x, randoms))
