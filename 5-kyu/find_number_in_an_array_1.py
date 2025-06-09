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

# tricky, use property that all numbers are from 1 to n - not random. just check if that numbers are mostly dupes or uniq, using probabilistic max_value property.
def duplicate_or_unique(inList):
    full_len = len(inList)
    sum_list = sum(inList)
    half_len = (full_len + 1) // 2
    max_value = max(inList)
    sum_on_uniq = half_len * (half_len + 1) // 2
    sum_on_dup = ((full_len - 1) * full_len) // 2 
    if max_value == full_len - 1:
        #print('one duplicate')
        return sum_list - sum_on_dup
    else:
        #print('one unique')
        return sum_on_uniq - (sum_list - sum_on_uniq)
