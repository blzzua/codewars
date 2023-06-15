# https://www.codewars.com/kata/5d472159d4f8c3001d81b1f8

from datetime import datetime, timedelta

def half_life(*persons):
    p1, p2 = sorted(map(lambda p: datetime(*map(int, p.split('-'))), persons))
    return (p2 + timedelta(days=(p2-p1).days)).strftime('%F')

