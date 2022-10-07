# https://www.codewars.com/kata/5624e574ec6034c3a20000e6

def hamming_distance(a, b):
    ret = 0
    for b1,b2 in zip(a,b):
        if b1 != b2:
            ret += 1
    return ret

