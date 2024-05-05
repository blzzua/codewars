# https://www.codewars.com/kata/5aceae374d9fd1266f0000f0

from datetime import datetime, timedelta
def time_math(time1, op, time2):
    basetime = int(datetime.strptime('00:00:00', '%H:%M:%S').strftime('%s'))
    t1 = int(datetime.strptime(time1, '%H:%M:%S').strftime('%s'))
    t2 = int(datetime.strptime(time2, '%H:%M:%S').strftime('%s'))
    if op == '+':
        delta = (t1 - basetime) + (t2 - basetime)
    elif op == '-':
        delta = (t1 - basetime) - (t2 - basetime)
    res = (datetime.strptime('00:00:00', '%H:%M:%S') + timedelta(seconds=delta)).strftime('%H:%M:%S')
    return res

