# https://www.codewars.com/kata/590a7f2be8e86e1240000068

def strange_code(s, e):
    res = ['a']
    while True:
        if s < e - 1:
            s += 1
            e -= 1
        else:
            return ''.join(res[:-1])
        if res[-1] == 'a':
            res.append('b')
        else:
            res.append('a')
