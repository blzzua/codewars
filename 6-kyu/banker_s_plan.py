# https://www.codewars.com/kata/56445c4755d0e45b8c00010a

def fortune(f0, p, c0, n, i):
    print(f"{f0=}, {p=}, {c0=}, {n=}, {i=}")
    f = f0
    c = c0
    p = p / 100
    i = i / 100
    
    for y in range(1, n):
        f0 = int(f0 + (p * f0) - c0)
        if f0 < 0:
            return False
        c0 = int(c0 + (c0 * i))
    return True
