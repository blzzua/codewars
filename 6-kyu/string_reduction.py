# https://www.codewars.com/kata/59fab1f0c9fc0e7cd4000072

from collections import Counter
def solve(a, b):
    # clever: if Counter(b) - Counter(a): return 0
    ca = Counter(a)
    cb = Counter(b)
    for letter in cb:
        if ca.get(letter) == 0:
            return 0
        if ca.get(letter, 0) < cb.get(letter):
            return 0
    return len(a) - len(b)

