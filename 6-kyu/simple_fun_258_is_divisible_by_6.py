# https://www.codewars.com/kata/5911385598dcd432ae000004

def is_divisible_by_6(s):
    if s[-1] in '13579':
        return []
    asterisk_position = s.index('*')
    l = list(s)
    l.remove('*')
    res_sum = sum(map(int,l))
    res = []
    for i in range(10):
        if (res_sum + i) % 3 == 0:
            if asterisk_position == len(s) - 1 and i % 2 == 1:
                continue
            candidate = s.replace('*',str(i))
            if candidate.startswith('0') and candidate != '0':
                candidate = candidate.lstrip('0')
            res.append(candidate)
    return res

