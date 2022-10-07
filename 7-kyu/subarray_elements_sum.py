# https://www.codewars.com/kata/5b5e0ef007a26632c400002a

def elements_sum(arr, d=0):
    s = 0
    for i, a in enumerate(arr[::-1]):
        if len(a) > i:
            s += a[i]
        else:
            s += d
    return s

