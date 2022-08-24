# https://www.codewars.com/kata/5bb50eb68f8bbdb4b300021d

from collections import Counter
from itertools import cycle
def distribute_evenly(lst):
    c = Counter(lst)
    res = []
    for w in cycle(c):
        if c[w] > 0 :
            res.append(w)
            c[w] -= 1
        if c.total() == 0:
            break
    return res
