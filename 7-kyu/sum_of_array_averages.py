# https://www.codewars.com/kata/56d5166ec87df55dbe000063

from statistics import mean
from math import floor
def sum_average(arr):
    return floor(sum(map(mean,arr)))

