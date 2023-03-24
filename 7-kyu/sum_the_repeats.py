# https://www.codewars.com/kata/56b4bae128644b5613000037

from collections import Counter
from itertools import chain
def repeat_sum(l):
    C = Counter(chain.from_iterable(list(set(inter_list)) for inter_list in l))
    return sum(i for i in C if C[i] > 1)
