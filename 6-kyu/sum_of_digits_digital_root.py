# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    while n > 9:
        n = sum(map(int,str(n)))
    return n
