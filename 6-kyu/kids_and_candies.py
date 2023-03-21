# https://www.codewars.com/kata/56cca888a9d0f25985000036

from math import gcd
def candies_to_buy(n):
    p = 1
    for i in range(2, n+1):
        p = p * i // gcd(p, i)
    return p
    
