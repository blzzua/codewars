# https://www.codewars.com/kata/58ad09d6154165a1c80000d1

def zero_and_one(s):
    l = list(s)
    c = len(l)
    i1, i2 = 0,1
    for i,(i1, i2) in enumerate(zip(l,l[1:])):
        if i1+i2 in ('01', '10'):
            l[i], l[i+1] = ' ', ' '
            c = c - 2
    return c # ''.join(l)


