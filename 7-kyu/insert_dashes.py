# https://www.codewars.com/kata/55960bbb182094bc4800007b

def insert_dash(num):
    num = list(str(num))
    res = [num[0]]
    for i, (d1, d2) in enumerate(zip(num, num[1:])):
        if d1 in '13579' and d2 in '13579':
            res.append('-')
        res.append(d2)
    return ''.join(res)

