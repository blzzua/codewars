# https://www.codewars.com/kata/58069e4cf3c13ef3a6000168

import math
def reverse(n):
    l = int(math.log(n,10))
    res = 0
    for i in range(l,-1,-1):
        rem, n = divmod(n,10**i) 
        res += 10 ** (l-i) * rem
    return res
        
        
        

