# https://www.codewars.com/kata/5a405ba4e1ce0e1d7800012e

from itertools import cycle
def custom_christmas_tree(chars, n):
    gen = cycle(chars)
    res = []
    for i in range(1,n+1):
        offset = n - i 
        res.append(' ' * offset + ' '.join(next(gen) for _ in range(i)))

    for i in range((n-3)//3+1):
        res.append(' ' * (n-1) + '|')
    return '\n'.join(res)
