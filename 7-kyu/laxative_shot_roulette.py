# https://www.codewars.com/kata/5b02ae6aa2afd8f1b4001ba4

def get_chance(n, x, a):
    res = 1
    for i in range(a):
        res = res * (1-x / (n-i))
    return round(res,2)
