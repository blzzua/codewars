# https://www.codewars.com/kata/5cc80fbe701f0d001136e5eb

from collections import defaultdict
def stem_and_leaf(data):
    res = defaultdict(list)
    for dig in data:
        d, rem = divmod(dig, 10)
        res[d].append(rem)
    sorted_keys = sorted(list(res.keys()))
    return {k: sorted(res[k]) for k in sorted_keys}
