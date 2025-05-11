# https://www.codewars.com/kata/62ce80a55487c16cba9957b3

def get_date(start, end, width, pos):
    ts = start+(end-start)*(pos/width)
    return ts.strftime('%Y-%m-%dT%H:%M')
