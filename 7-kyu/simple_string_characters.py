# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058

def solve(s):
    u,l,n,o = 0,0,0,0
    for c in s:
        if c.isupper():
            u += 1
        elif c.islower():
            l += 1
        elif c.isdigit():
            n += 1
        else:
            o += 1
    return [u,l,n,o]

