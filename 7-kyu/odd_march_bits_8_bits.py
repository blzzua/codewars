# https://www.codewars.com/kata/58ee4db3e479611e6f000086

def bit_march (n : int) -> list:
    return [[int(8-n-1< i+j <8) for j in range(8)] for i in range(8-n+1)]


