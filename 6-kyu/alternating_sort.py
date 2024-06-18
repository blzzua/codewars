# https://www.codewars.com/kata/5ac49156376b11767f00060c

def alternate_sort(l):
    pos = sorted([*filter(lambda x: x>=0, l)], reverse=True)
    neg = sorted([*filter(lambda x: x<0, l)])
    res = []
    while pos + neg:
        if neg:
            res.append(neg.pop())
        if pos:
            res.append(pos.pop())
    return res

