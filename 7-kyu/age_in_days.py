# https://www.codewars.com/kata/5803753aab6c2099e600000e

from datetime import date

def age_in_days(year, month, day):
    days = (date.today()-(date(year=year, month=month, day=day))).days
    if days > 0:
        return f'You are {days} days old'

