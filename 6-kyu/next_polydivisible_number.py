# https://www.codewars.com/kata/5e4a1a43698ef0002d2a1f73
# https://oeis.org/A144688

def is_polydivisible(n):
    s = str(n)
    for p in range(1, len(s) + 1):
        if int(s[:p]) % p != 0:
            return False
    return True

def next_num(n):
    if n > 3608528850368400786036724:
        return None
    n = int(n)+1
    while not is_polydivisible(n):
        s = str(n)
        l = len(s)
        for p in range(2, len(s)+1):
            if (int(s[:p]) % p) > 0:
                n = 10 ** (l-p) * (int(s[:p]) + (p - int(s[:p]) % p))
            s = str(n)
            if l != len(s): break
    return n

