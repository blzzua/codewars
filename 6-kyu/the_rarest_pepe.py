# https://www.codewars.com/kata/595d4823c31ba629d90000d2

from collections import Counter

def find_rarest_pepe(pepes):
    print(pepes)
    c = Counter(pepes)
    rarest_cnt = min(c.values())
    if rarest_cnt >= 5:
        return 'No rare pepes!'
    res = sorted(filter(lambda x: c[x] == rarest_cnt, c))
    if len(res) == 1:
        return res[0]
    return res
