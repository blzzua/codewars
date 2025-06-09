# https://www.codewars.com/kata/583ef2456e39941f810001c5
# works but not pass perf tests
from collections import Counter
def duplicate_or_unique(inList):
    c = Counter(inList)
    q = Counter(c.values())
    dup_or_uniq = next(i for i in (1,2) if q.get(i) == 1)
    return next(filter(lambda x: c.get(x) == dup_or_uniq, c))

