# https://www.codewars.com/kata/55fb6537544ae06ccc0000dc

def summary_ranges(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [str(arr[0])]
    res = []
    prev = arr[0]
    a = [prev,]
    for i in arr:
        if i == prev:
            continue
        else:
            a.append(i)
            prev = i
    i = 0
    while i < len(a):
        num = a[i]
        while i + 1 < len(a) and a[i + 1] - a[i] == 1:
            i += 1
        if a[i] != num:
            res.append(f'{num}->{a[i]}')
        else:
            res.append(str(num))
        i += 1
    return res



