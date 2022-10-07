# https://www.codewars.com/kata/585a033e3a36cdc50a00011c

from collections import Counter
def freq_seq(s, sep):
    c = Counter(s)
    return sep.join([str(c[char]) for char in s])
         


