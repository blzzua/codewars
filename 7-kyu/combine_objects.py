# https://www.codewars.com/kata/56bd9e4b0d0b64eaf5000819

from collections import Counter
def combine(*dicts):
    res = Counter()
    for d in dicts:
        res = res + Counter(d)
    return dict(res)

    

