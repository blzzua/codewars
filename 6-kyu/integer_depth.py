# https://www.codewars.com/kata/59b401e24f98a813f9000026

def compute_depth(n):
    seen = set()
    i = 0
    while len(seen) < 10:
        i+=1
        seen = seen.union({digit for digit in str(n * i)})
    return i
