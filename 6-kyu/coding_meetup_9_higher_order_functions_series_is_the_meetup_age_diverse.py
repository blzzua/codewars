# https://www.codewars.com/kata/5829ca646d02cd1a65000284

from collections import Counter
def is_age_diverse(lst): 
    must = Counter([1,2,3,4,5,6,7,8,9])
    c = Counter(min(o['age'], 100) // 10 for o in lst)
    return not bool(must - c)
