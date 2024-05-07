# https://www.codewars.com/kata/580ec64394291d946b0002a1

def mysterious_pattern(m, n):
    print(m,n)
    i = m
    a, b = 1, 1
    fib = [a%n,]
    while i > 1:
        a, b, i = b, a + b, i - 1
        fib.append(a % n)
    res = []
    for r in range(n):
        line = ''.join('o' if i == r else ' ' for i in fib)
        res.append(line.rstrip())
    return '\n'.join(res).rstrip().lstrip('\n')
