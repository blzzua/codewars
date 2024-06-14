# https://www.codewars.com/kata/565c4e1303a0a006d7000127

def number_format(n):
    sign = '' if n >= 0 else '-'
    res = []
    n = abs(n)
    while n > 0:
        n, rem = divmod(n, 1000)
        res.append(str(rem).zfill(3))
    return sign + (','.join(res[::-1])).lstrip('0')

# actual solution:
# return f'{n:,}'
