# https://www.codewars.com/kata/5e2596a9ad937f002e510435

def infected(s):
    continents = s.split('X')
    tot = sum(len(c) for c in continents)
    inf = sum(len(c) for c in continents if '1' in c)
    if tot > 0:
        return inf * 100 / tot
    else:
        return 0

