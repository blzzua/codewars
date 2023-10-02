# https://www.codewars.com/kata/59aa6567485a4d03ff0000ca

from gmpy2 import next_prime, is_prime

def is_ends_1(n):
    t = [n]
    while t.index(n) == len(t) - 1 and n != 1:
        n = sum(i * i for i in map(int,str(n)))
        t.append(n)
    return n == 1
    
def solve(a,b):
    cnt = 0
    i = a - 1
    while True:
        i = next_prime(i)
        if i >= b:
            break
        if is_ends_1(i):
            cnt += 1
    return cnt
