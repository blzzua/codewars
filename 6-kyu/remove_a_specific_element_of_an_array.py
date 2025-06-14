# https://www.codewars.com/kata/581bb3c1c221fb8e790001ef

from math import prod

def select_subarray(arr):
    sum_ = sum(arr)
    prod_ = prod(arr)

    sub_arr = []
    for i, n in enumerate(arr):
        if sum_ - n == 0:
            continue
        ratio = abs(prod_ / n / (sum_ - n))
        sub_arr.append([i, ratio])
    sub_arr.sort(key=lambda x: x[1])

    if not sub_arr:
        return []

    res = [[i, arr[i]] for i, ratio in sub_arr if ratio == sub_arr[0][1]]
    if len(res) == 1:
        return res[0]
    else:
        return res
