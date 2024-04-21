# https://www.codewars.com/kata/569f6ad962ff1dd52f00000d

def sel_quot(arr, m, dir_str = 'default'):
    res = []
    for i, a in enumerate(arr):
        for j, b in enumerate(arr):
            if i == j:
                continue
            if a % b:
                continue
            divisor = a // b
            if divisor < m:
                continue
            if (dir_str == 'default' or (dir_str.lower() == 'even' and divisor % 2 == 0) or (dir_str.lower() == 'odd' and divisor % 2 == 1)):
                min_val, max_val = sorted((a, b))
                if all(d[0] != divisor or d[1][0] != max_val or d[1][1] != min_val for d in res):
                    res.append( (int(divisor), (max_val, min_val)))
    return sorted(res)
