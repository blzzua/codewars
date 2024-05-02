# https://www.codewars.com/kata/51f1342c76b586046800002a

def solution(n):
    n, d = divmod(n,1)
    return n + (((d >= 0.25) + (d >= 0.75)))/2
