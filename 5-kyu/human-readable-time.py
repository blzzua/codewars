# https://www.codewars.com/kata/52685f7382004e774f0001f7
def make_readable(seconds):
    m,s = divmod(seconds,60)
    h,m = divmod(m,60)
    return ':'.join([str(i).zfill(2) for i in (h,m,s)])
