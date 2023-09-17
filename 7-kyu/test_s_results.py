# https://www.codewars.com/kata/599db0a227ca9f294b0000c8

from statistics import mean
def test(r):
    levels = {'h': 0, 'a': 0, 'l': 0}
    sum_ = 0
    for i in r:
        sum_ += i
        if i in (9, 10):
            levels['h'] += 1
        elif i in (7, 8):
            levels['a'] += 1
        elif 1 <= i <= 6:
            levels['l'] += 1
    avg = round(sum_/len(r), 3)
    res = [avg, levels]
    if levels['h'] == len(r):
        res.append('They did well')
    return res
