# https://www.codewars.com/kata/5885b5d2b632089dc30000cc

from datetime import date
def day_of_week(dt):
    WEEKDAYS = {1: 'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
    return WEEKDAYS[date(*map(int,dt.split('/')[::-1])).isoweekday()]
