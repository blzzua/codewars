# https://www.codewars.com/kata/55c11989e13716e35f000013

def stringify(i):
    return '0' if i == 0 else '1'

def initify(i):
    return 0 if i == '0' else 1

def add(a,b):
    a = list(a)
    b = list(b)
    pad = 0
    res = []
    while a or b:
        p1 = a.pop() if a else '0'
        p2 = b.pop() if b else '0'
        p1 = initify(p1) 
        p2 = initify(p2) 
        pad, p3 = divmod(p1 + p2 + pad, 2)
        res.append(stringify(p3))
    if pad: 
        res.append(stringify(pad))
    return ''.join(res[::-1]).lstrip('0') or '0'
  
