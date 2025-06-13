# https://www.codewars.com/kata/5907f9032e5646e409000001

from collections import defaultdict
def pro_categorization(pros, preferences):
    categories = defaultdict(list)
    for pro, pref in zip(pros, preferences):
        for cat in pref:
            categories[cat].append(pro)
    
    res = [[[cat,], sorted(categories[cat])] for cat in sorted(dict(categories))]
    return res
