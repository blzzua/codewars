# https://www.codewars.com/kata/588856a82ffea640c80000cc

def array_previous_less(arr):
    res = []
    for i, v in enumerate(arr):
        for j in range(i - 1, -1, -1):
            if arr[j] < v:
                res.append(arr[j])
                break
        else:
            res.append(-1)
    return res
