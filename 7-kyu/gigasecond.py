# https://www.codewars.com/kata/53f99455573c064ad200010b

from datetime import datetime, date, timedelta
def gigasecond(start_date):
    res = (start_date + timedelta(seconds = 10**9))
    return date(res.year,res.month,res.day)
