# https://www.codewars.com/kata/5603a4dd3d96ef798f000068

from math import prod

def share_price(invested, changes):
    res = round(invested * prod(1.0 + c / 100.0 for c in changes),2)
    return '{:.02f}'.format(res)
