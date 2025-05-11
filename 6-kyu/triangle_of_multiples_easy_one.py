# https://www.codewars.com/kata/58ecc0a8342ee5e920000115

def mult_triangle(n):
    total = (n*(n+1)//2)**2
    odds = ((n+1)//2)**4
    even = total - odds
    return [total, even, odds]
