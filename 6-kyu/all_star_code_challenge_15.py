# https://www.codewars.com/kata/586560a639c5ab3a260000f3

def rotate(str_):
    l = len(str_)
    s = str_ + str_
    return [ (s[i:]+s[:i])[:l] for i in range(1, l+1)]


# this kata can be solved with collections.deque
import collections
def rotate(str_):
    queue = collections.deque(str_)
    return [queue.rotate(-1) or ''.join(queue) for _ in str_]
