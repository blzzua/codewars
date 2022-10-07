# https://www.codewars.com/kata/5412509bd436bd33920011bc

import re
def maskify(cc):
    if len(cc) <= 4:
        return cc
    return re.sub('.', '#', cc, len(cc)-4)

