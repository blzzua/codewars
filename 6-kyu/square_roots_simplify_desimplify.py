# https://www.codewars.com/kata/5850e85c6e997bddd300005d

def simplify(n):
    q = 1
    for i in range(int(n ** 0.5) +1, 1, -1):
        if n % (i*i) == 0:
            q = i
            n = n // q //q
            break
    res = []
    if q != 1:
        res.append(str(q))
    if n != 1:
        res.append('sqrt ' + str(n))
    return ' '.join(res) or '1'

def desimplify(s):
    dig,_, sq = s.partition('sqrt ')
    if dig:
        res = int(dig)**2
    else:
        res=1
    if sq:
        res = res * int(sq)
    return res 
