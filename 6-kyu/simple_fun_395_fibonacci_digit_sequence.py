# https://www.codewars.com/kata/5bc555bb62a4cec849000047

def find(a,b,n):
    print(f'{a=},{b=}, {n=}')
    if a + b == 0:
        return 0
    if n == 0:
        return a
    if n == 1:
        return b
    if n > 100:
        n = n % 80 + 20 # here you can find is some types of cycles. 
    c = 0
    while n > 1:
        c = a + b
        if c < 10:
            a, b = b, c
            n = n - 1
        else:
            a, b = divmod(c,10)
            n = n - 2
    if n == 0:
        return a
    if n == 1:
        return c % 10
