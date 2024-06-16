# https://www.codewars.com/kata/5286b2e162056fd0cb000c20

def collatz(n):
    res = str(n)
    while n > 1:
        n = (3 * n + 1) if n % 2 else (n // 2)
        res = res + f'->{n}'
    return res
