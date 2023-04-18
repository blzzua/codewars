# https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc

from collections import Counter
def solve(arr):
    c = Counter(arr)
    res = []
    for item, cnt, in sorted(c.items(), key=lambda x : (-x[1], x[0])):
        res.extend([item] * cnt)
    return res

