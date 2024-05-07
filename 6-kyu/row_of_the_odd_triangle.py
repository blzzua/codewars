# https://www.codewars.com/kata/5d5a7525207a674b71aa25b5

def odd_row(n):
    return  [*range(n**2-n+1, (n+1)**2-n, 2)]
