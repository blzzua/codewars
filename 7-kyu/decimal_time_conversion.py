# https://www.codewars.com/kata/6397b0d461067e0030d1315e

def to_industrial(time):
    if ':' in str(time):
        m, s = time.split(":")
        m, s = int(m), int(s)
    else:
        m, s = 0, time
    return round(m + s / 60, 2)

def to_normal(time):
    m, s = divmod(time, 1 )
    m, s = int(m), round(s * 60)
    return f'{m}:{s:02d}'
