# https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d

def halving_sum(n): 
    s = 0
    while n > 0:
        s += n
        n = n // 2 
    return s

