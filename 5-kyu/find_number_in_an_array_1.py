# https://www.codewars.com/kata/583ef2456e39941f810001c5
# works but not pass perf tests
from collections import Counter
def duplicate_or_unique(inList):
    c = Counter(inList)
    q = Counter(c.values())
    dup_or_uniq = next(i for i in (1,2) if q.get(i) == 1)
    return next(filter(lambda x: c.get(x) == dup_or_uniq, c))


# probable better time solution. avg time 8.5ms, but can be longer.
def duplicate_or_unique(inList):
    list_len = len(inList)
    uniq_len = len(set(inList))
    if list_len == uniq_len * 2 - 1:
        uniq = 0
        for v in inList:
            uniq = uniq ^ v
        return uniq
    else: 
        seen = set()
        for v in inList:
            if not v in seen: 
                seen.add(v)
            else:
                return v
