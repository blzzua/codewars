# https://www.codewars.com/kata/588e10c5f051b147ff00004b

def close_to_zero(t):
    seq = list(map(int,t.split()))
    m = min(seq, key=lambda x: abs(x-0),default=0)
    if m < 0 and -m in seq:
        return -m
    return m
