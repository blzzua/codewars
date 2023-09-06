# https://www.codewars.com/kata/64f41ad92b610b64c1067590

def full_cycle(lst):
    i = 0
    res = set()
    for _ in lst:
        i = lst[i]
        res.add(i)
    return len(res) == len(lst)
