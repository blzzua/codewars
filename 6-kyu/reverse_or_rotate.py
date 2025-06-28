# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991

def rot(s):
    return s[1:] + s[0]

def rev(s):
    return s[::-1]

def rev_rot(strng, sz):
    if sz == 0:
        return ''
    res = ''
    for i in range(0, len(strng), sz):
        ch = strng[i:i+sz]
        if len(ch) != sz:
            break
        res += [rev(ch), rot(ch)][sum(map(int,ch)) % 2]
    return res

