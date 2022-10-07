# https://www.codewars.com/kata/528e95af53dcdb40b5000171

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    r = 1
    for i in range(1,n+1):
        r *= i
    return r
    


