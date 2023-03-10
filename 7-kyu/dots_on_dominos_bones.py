# https://www.codewars.com/kata/6405f2bb2894f600599172fd

def dots_on_domino_bones(n):
    if n < 0:
        return -1
    res = 0 
    for k in range(n+1):
        res +=  k*(n-k+1) + (k+n)*(n-k+1)//2
    return res
