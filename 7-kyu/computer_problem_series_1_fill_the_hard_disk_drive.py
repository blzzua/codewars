# https://www.codewars.com/kata/5d49c93d089c6e000ff8428c

def save(sizes, hd):
    summ=0
    i = 0
    res = len(sizes)
    for i,s in enumerate(sizes):
        summ = summ + s
        if summ > hd:
            res = i
            break
    return res

