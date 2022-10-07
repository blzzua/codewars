# https://www.codewars.com/kata/53f103c3ef9ad4014f00013b

from collections import Counter
def find_most_frequent(l):
    return {k for k,v in Counter(l).items() if v == max(Counter(l).values())}

