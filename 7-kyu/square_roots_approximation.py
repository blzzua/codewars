# https://www.codewars.com/kata/58475cce273e5560f40000fa

def approx_root(n):
    base = int(n ** 0.5)
    down = base ** 2
    up = (base + 1) ** 2
    return round(base + (n - down) / (up - down), 2)

