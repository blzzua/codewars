# https://www.codewars.com/kata/5d629a6c65c7010022e3b226

def parsetime(t):
    h, _, mplus = t.partition(':')
    m, ampm = mplus[:2], mplus[2:]
    if h == '12': 
        h = '0'
    h = int(h)
    m = int(m)
    if ampm == 'pm':
        h = int(h) + 12
    return h + (m/60)

def get_hours(shifts):
    res = []
    for t1, t2 in shifts:
        diff = round( 4 * (parsetime(t2) - parsetime(t1)) ) / 4
        if diff < 0:
            diff = 24 + diff
        res.append(diff)
    return res
