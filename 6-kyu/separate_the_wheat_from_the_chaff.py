# https://www.codewars.com/kata/5bdcd20478d24e664d00002c

def wheat_from_chaff(values):
    size = len(values)
    res = values[:]
    head, tail = 0, size - 1
    while head <= tail:
        if values[head] < 0:
            res[head] = values[head]
            head +=1
        elif values[tail] > 0:
            res[tail] = values[tail]
            tail -=1
        else:
            res[tail], res[head] = values[head], values[tail]
            head, tail = head + 1, tail - 1
    return res
