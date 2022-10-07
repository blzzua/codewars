# https://www.codewars.com/kata/57cec34272f983e17800001e

def pop_shift(s):
    l = len(s)
    s = list(s)
    b,e,m = [],[],[]
    for i in range(l//2):
        b.append(s.pop())
        e.append(s.pop(0))
    return [''.join(b), ''.join(e),''.join(s)]

