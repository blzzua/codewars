# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3

from collections import Counter
def find_uniq(arr):
    brr = [frozenset(Counter(w.lower()).keys()) for w in arr]
    return arr[brr.index(Counter(brr).most_common(2)[1][0])]
