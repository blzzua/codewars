# https://www.codewars.com/kata/56f19a230cd8bc5814001047

from datetime import timedelta

def week_start_date(dt):
    return dt - timedelta(dt.weekday())

def week_end_date(dt):
    return week_start_date(dt) + timedelta(6)

