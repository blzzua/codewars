# https://www.codewars.com/kata/61055e2cb02dcb003da50cd5

from itertools import combinations
def pair_items(list1, list2):
    res = []
    if len(list1) < len(list2):
        for comb in combinations(list2, len(list1)):
            res.append(list(zip(list1,comb)))
    else:
        for comb in combinations(list1, len(list2)):
            res.append(list(zip(comb,list2)))
    return res
