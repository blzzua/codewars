# https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4

def least_larger(a, i): 
    ret = sorted(e for e in a if e > a[i])
    if ret:
        return a.index(ret[0])
    else:
        return -1

