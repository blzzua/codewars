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



# optimized by Unnamed:
def summary_ranges(xs):
    res = []
    i = 0
    while i < len(arr):
        j = i
        while j + 1 < len(arr) and arr[j + 1] - arr[j] <= 1:
            j += 1
        res.append(str(arr[i]) if arr[i] == arr[j] else f'{arr[i]}->{a[j]}')
        i = j + 1
    return res   
