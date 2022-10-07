# https://www.codewars.com/kata/5250a89b1625e5decd000413

def flatten(lst):
    ret = []
    for el in lst:
        ret.extend(el) if type(el) == list else ret.append(el)
    return ret

