# https://www.codewars.com/kata/624e0a4c3e1d7b0031588666

def recurrence(values):
    prev, cnt = 0, -1
    values = values[values.index(min(values)):]

    for i, val in enumerate(values):
        if val > prev:
            cnt += 1
        else:
            cnt = 0
        prev = val
        if cnt > 2:
            return True
    return False


# clever
def recurrence(values):
    idx = values.index(min(values))
    return any(a < b < c < d for a, b, c, d in zip(*(values[idx + a:] for a in range(4))))
