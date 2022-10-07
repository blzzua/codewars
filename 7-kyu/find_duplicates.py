# https://www.codewars.com/kata/5558cc216a7a231ac9000022

def duplicates(array):
    s = set()
    res = []
    for a in array:
        if a not in res and a in s:
            res.append(a)
        s.add(a)
    return res

