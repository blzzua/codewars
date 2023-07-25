# https://www.codewars.com/kata/631082840289bf000e95a334

def max_int_chain(n):
    if n < 5: return -1
    res = n // 2
    c, d = res + (-1) ** ((n+1)%2),  res + (1-n%2)
    return c * d 
