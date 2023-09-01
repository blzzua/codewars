# https://www.codewars.com/kata/586d12f0aa042830910001d1

def clean(s):
    is_ds = False # dollar sign
    is_point = False
    res = []
    for c in s:
        if c.isdecimal():
            res.append(c)
    res.insert(-2, '.')
    res.insert(0, '$')
    return ''.join(res)

def remove_char(array):
    return list(map(clean, array))
