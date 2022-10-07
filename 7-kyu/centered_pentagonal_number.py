# https://www.codewars.com/kata/5fb856190d5230001d48d721

def pentagonal(n):
    if n > 0:
        return 1 + 5 * (n - 1) * n // 2 
    else:
        return -1

