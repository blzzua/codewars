# https://www.codewars.com/kata/5a8d1c82373c2e099d0000ac

def solve(st,a,b):
    b = min(len(st),b) + 1 
    return st[:a] + st[a:b][::-1] + st[b:]
