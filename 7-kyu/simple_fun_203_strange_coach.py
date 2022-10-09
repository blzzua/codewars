# https://www.codewars.com/kata/58fd91af13b0012e8e000010

from collections import Counter
def strange_coach(players):
    c = Counter(map(lambda x: x[0],players))
    res = ''.join(sorted(filter(lambda x: c[x]>=5, c)))
    return res or 'forfeit'
