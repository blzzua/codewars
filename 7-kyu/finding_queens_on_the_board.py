# https://www.codewars.com/kata/64060d8ab2dd990058b7f8ee

def queens(n):
    k = 0 if n < 2 else n - 1 
    return k ** 5 // (k ** 3 + k ** 2 + 1)
