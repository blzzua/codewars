# https://www.codewars.com/kata/554ca54ffa7d91b236000023

from collections import Counter
def delete_nth(order,max_e):
    d = {}
    res = []
    for item in order:
        d[item] = d.get(item,0) + 1 
        if d[item] <= max_e:
            res.append(item)
    return res

