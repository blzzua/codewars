# https://www.codewars.com/kata/58aa6141c9eb047fec000133

def survivor(n):
    i = 2 
    while i <= n:
        if n%i == 0:
            return False
        n = n-n//i
        i += 1
    return True
