# https://www.codewars.com/kata/64ef24b0679cdc004d08169e

def min_turns(current, target):
    res = 0
    for c, t in zip(str(current), str(target)):
        c, t = int(c), int(t)
        forward = min(abs(t - c), abs(c - t + 10 ))
        backward = min(abs(t - c), abs(t + 10 - c))
        res += min(forward, backward)
    return res
