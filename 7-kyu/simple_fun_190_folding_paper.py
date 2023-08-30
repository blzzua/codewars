# https://www.codewars.com/kata/58bfa1ea43fadb41840000b4

def folding(a,b):
    c = 0
    while b > 0:
        c, b, a = c + 1, max(a,b) - min(a,b), min(a,b)
    return c
    
