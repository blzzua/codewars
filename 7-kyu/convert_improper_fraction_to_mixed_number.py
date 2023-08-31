# https://www.codewars.com/kata/584acbee7d22f84dc80000e2

def get_mixed_num(fraction):
    f1,f2 = map(int,fraction.split('/'))
    p1,p2 = divmod(f1,f2)
    return f'{p1} {p2}/{f2}'
