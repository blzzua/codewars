# https://www.codewars.com/kata/5a31a71c1f7f705a93000005

from itertools import cycle
def gen(n, iterable):
    g = cycle(iterable)
    buf = []
    for i in range(n):
        buf.append(next(g))
    while True:
        yield tuple(buf)
        buf.pop(0)
        buf.append(next(g))

# this kata can be solved with deque
from collections import deque
def gen(n, iterable):
    g = cycle(iterable)
    buf = deque([buf.append(next(g)) for i in range(n)], maxlen=n)     # buf = deque(islice(cycle(iterable), n), maxlen=n)
    while True:
        yield tuple(buf)
        buf.append(next(g))
