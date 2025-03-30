# https://www.codewars.com/kata/58999425006ee3f97c00011f

from statistics import mean, StatisticsError

def passed(lst):
    try:
        return round(mean([i for i in lst if i <= 18]))
    except StatisticsError:
        return 'No pass scores registered.'
