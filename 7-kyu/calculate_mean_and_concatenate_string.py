# https://www.codewars.com/kata/56f7493f5d7c12d1690000b6

def mean(lst):
    s, d = [], []
    for c in lst:
        if c.isnumeric():
            d.append(int(c))
        else:
            s.append(c)
    return [ sum(d)/len(d) ,''.join(s)]
