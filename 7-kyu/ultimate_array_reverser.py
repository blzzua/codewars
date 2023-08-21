# https://www.codewars.com/kata/5c3433a4d828182e420f4197

from collections import deque

def reverse(a):
    q = deque(''.join(a))
    return [''.join(q.pop() for _ in range(l)) for l in map(len,a)]
