# https://www.codewars.com/kata/58afce23b0e8046a960000eb

def withdraw(n):
    res_50 = 0
    res_20, n = divmod(n, 20)
    if n == 10:
        res_50, res_20 = 1, res_20 - 2
    res_100, res_20 = divmod(res_20, 5)
    return [res_100, res_50, res_20]

#clever:
def withdraw(n):
    res20 = 0
    while n % 50:
        res20 += 1
        n -= 20
    return [n // 100, (n % 100) // 50, res20]
