# https://www.codewars.com/kata/5aee96e22c5061ee90000024

def quadratic_gen(a,b,c, start=0, step=1):
    for i in range(10):
        x = start + step * i
        y = a * (x ** 2) + b * x + c
        yield [x,y]
