# https://www.codewars.com/kata/56eb16655250549e4b0013f4

import calendar 
from collections import Counter
def most_frequent_days(year):
    weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_in_year = 366 if calendar.isleap(year) else 365
    first = calendar.weekday(year, 1, 1)
    #     correct ordering        actual data                                                                       balance of added ordering
    res = Counter(weekday_names) + Counter([weekday_names[i % 7] for i in range(first, first+days_in_year - 52*7)]) - Counter(weekday_names)
    return list((res).keys())
