# https://www.codewars.com/kata/55d8aa568dec9fb9e200004a

def sel_number(n, d):
    res = 0
    for i in range(12, n + 1):
        s = list(map(int, str(i)))
        increasing = False
        for a, b in zip(s, s[1:]):
            if 0 < b - a <= d:
                increasing = True
            else:
                increasing = False
                break
        if increasing: 
            res += 1
    return res

