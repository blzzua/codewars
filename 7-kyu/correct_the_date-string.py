# https://www.codewars.com/kata/5787628de55533d8ce000b84

import re
import datetime

def date_correct(date):
    if not date:
        return date
    m = re.match("(\d\d)\.(\d\d)\.(\d{4})", date)
    if not m:
        return None
    d, m, y = map(int, m.groups())
    plus_y, m = divmod(m, 12)
    y += plus_y
    if m == 0:
        m = 12
        y -= 1
    res_date = datetime.date(y, m, 1) + datetime.timedelta(days = d - 1)
    res = res_date.strftime('%d.%m.%Y')
    return res
