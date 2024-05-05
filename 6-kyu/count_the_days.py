# https://www.codewars.com/kata/5837fd7d44ff282acd000157

import datetime
def count_days(d):
    print(d)
    now = datetime.datetime.today()
    diff = (d - datetime.datetime(now.year, now.month, now.day))
    if diff.days < 0:
        return 'The day is in the past!'
    elif diff.days == 0:
        return  'Today is the day!'
    else:
        if d.hour <= 4: # timezone issues ?
            diff_int  = diff.days - 1
        else:
            diff_int  = diff.days
        return str(diff_int) + ' days'

