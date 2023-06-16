# https://www.codewars.com/kata/58a6742c14b042a042000038

def S2N(m, n):
    return sum(i**j for i in range(m+1) for j in range(n+1))
