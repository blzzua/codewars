# https://www.codewars.com/kata/5af974846bf32304a2000e98

from collections import Counter
def majority(arr):
    c = Counter(arr)
    if len(c) == 1:
        return c.most_common(1)[0][0]
    elif len(c) > 1:
        mc = c.most_common(2)
        if mc[0][1] != mc[1][1]:
            return c.most_common(1)[0][0]
    

