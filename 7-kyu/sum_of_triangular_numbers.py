# https://www.codewars.com/kata/580878d5d27b84b64c000b51

def sum_triangular_numbers(n):
    return sum(i*(i+1)/2 for i in range(n+1))

