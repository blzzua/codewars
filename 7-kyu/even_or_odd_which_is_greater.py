# https://www.codewars.com/kata/57f7b8271e3d9283300000b4

def even_or_odd(s):
    res = [0,0]
    for d in s:
        res[int(d)%2] += int(d)
    even, odd = res
    return {even == odd: 'Even and Odd are the same',
    even > odd: 'Even is greater than Odd',
    even < odd: 'Odd is greater than Even'}[True]


