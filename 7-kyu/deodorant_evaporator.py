# https://www.codewars.com/kata/5506b230a11c0aeab3000c1f

from math import ceil, log
def evaporator(content, evap_per_day, threshold):
    threshold /= 100
    return ceil(log((threshold))/log((100-evap_per_day)/100))

