# https://www.codewars.com/kata/5aec1ed7de4c7f3517000079

def first_n_smallest(arr, n):
    if n == 0:
        return []
    threshold_value = sorted(arr)[n-1]
    res = [i for i in arr if i <= threshold_value ]
    while len(res) > n:
        out_value = max(res)
        for i in range(len(res) -1, -1, -1):
            if res[i] == out_value:
                res.pop(i)
                break
    return res


# same but compact version
m = sorted(arr)[:n]
return [m.pop(m.index(i)) for i in arr if i in m]
