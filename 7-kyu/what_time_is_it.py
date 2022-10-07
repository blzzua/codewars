# https://www.codewars.com/kata/57729a09914da60e17000329

def get_military_time(time):
    h,m,s = time.split(':')
    if s.endswith('PM'):
        if h!='12':
            h=str(int(h)+12).zfill(2)
    else:
        h=str(int(h)%12).zfill(2)
    s=s[0:2]
    return ':'.join((h,m,s))


