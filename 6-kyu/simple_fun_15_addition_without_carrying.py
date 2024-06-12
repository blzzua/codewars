# https://www.codewars.com/kata/588468f3b3d02cf67b0005cd

def addition_without_carrying(a, b):
    s1 = str(a).zfill(6)
    s2 = str(b).zfill(6)
    res = ''.join(str((int(d1)+int(d2)) % 10) for d1, d2 in zip(s1, s2))
    return int(res)


# pretty solution without int<->str convertion:
def addition_without_carrying(a,b):
    res = 0
    exp = 1
    while a+b:
        res += ( a+b ) % (10*m)
        exp *= 10
        a //= 10
        b //= 10
    return res
