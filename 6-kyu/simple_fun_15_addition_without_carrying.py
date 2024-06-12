# https://www.codewars.com/kata/588468f3b3d02cf67b0005cd

def addition_without_carrying(a, b):
    s1 = str(a).zfill(6)
    s2 = str(b).zfill(6)
    res = ''.join(str((int(d1)+int(d2)) % 10) for d1, d2 in zip(s1, s2))
    return int(res)
