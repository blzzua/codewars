# https://www.codewars.com/kata/581963edc929ba19e7000148

def furthest_distance(arr, k):
    res = []
    for j, val1 in enumerate(arr):
        for i, val2 in enumerate(arr[j:],j):
            if abs(val2-val1) >= k:
                res.append(abs(i-j))
    if res:
        return max(res)
    else:
        return -1
