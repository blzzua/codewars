# https://www.codewars.com/kata/5521d84b95c172461d0000a4

def to_bcd(n):
    sign = '-' if n < 0 else ''
    res = []
    n = abs(n)
    while True:
        n, rem = divmod(n, 10)
        res.append(f'{rem:04b}')
        if n == 0:
            break
    return sign + ' '.join(res[::-1])
