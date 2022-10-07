# https://www.codewars.com/kata/588e27b7d1140d31cb000060

def generate_pairs(n):
    res = []
    [[res.append([a,b])  for b in range(a,n+1)] for a in range(n+1)]
    return res

