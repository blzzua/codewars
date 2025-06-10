# https://www.codewars.com/kata/58acf6c20b3b251d6d00002d

def rocks(n):
    l = len(str(n))
    b = 10 ** (l-1)
    cnt = n + 1 - b
    prev = sum(9 * i * 10 ** (i - 1) for i in range(1, l))
    return cnt * l + prev

