# https://www.codewars.com/kata/5a21e090f28b824def00013c

from collections import defaultdict

def switch_dict(dic):
    res = defaultdict(list)
    for k, v in dic.items():
        res[v].append(k)
    return res

