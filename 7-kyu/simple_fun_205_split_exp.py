# https://www.codewars.com/kata/58fd9f6213b00172ce0000c9

def split_exp(n):
    lenn = len(n)
    res  = []
    pnt = n.find('.')
    if pnt < 0:
        res = [c + '0'*(lenn-i-1) for i, c in enumerate(n) if c != '0']
    else:
        for i,j in zip(range(0, pnt), range(pnt-1,-1,-1)):
            if n[i]!= '0': res.append(n[i] + '0'*j)
        for i, j in zip(range(pnt+1, lenn), range(lenn)):
            if n[i]!= '0': res.append('.' + '0'*j + n[i])
    return res
