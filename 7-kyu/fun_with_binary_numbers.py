# https://www.codewars.com/kata/5ce04eadd103f4001edd8986

def solution(n,b):
    return [ i for i in range(2**n) if b == i & b and b != 0]
