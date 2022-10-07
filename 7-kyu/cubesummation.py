# https://www.codewars.com/kata/550e9fd127c656709400024d

def cube_sum(n, m):
    return sum(x ** 3 for x in range(min(n, m) + 1, max(n, m) + 1))

