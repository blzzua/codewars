# https://www.codewars.com/kata/58ac1abdff4e78738f000805

from collections import Counter, defaultdict

def the_biggest_search_keys(*keys):
    if len(keys) == 0:
        return "''"
    res = defaultdict(list)
    for k in keys:
        res[len(k)].append(k)
        max_key_len = max(res.keys())
    return ', '.join(f"'{word}'" for word in sorted(res[max_key_len]))
