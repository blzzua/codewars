# https://www.codewars.com/kata/5893f43b779ce54da4000124

def array_change(arr):
    a = arr[:]
    accum = 0
    for i, (prev, cur) in enumerate(zip(a,a[1:]),1):
        # print(a, i, prev, cur)
        if prev >= cur:
            accum += prev - cur + 1
            a[i] = prev + 1
    return accum
