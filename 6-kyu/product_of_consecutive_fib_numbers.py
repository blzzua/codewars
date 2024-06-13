# https://www.codewars.com/kata/5541f58a944b85ce6d00006a

def product_fib(_prod):
    f1 = 0
    f2 = 1
    while True:
        if f1 * f2 >= _prod:
            return [f1,f2, _prod == f1 * f2]
        f1, f2 = f2, f1+f2
