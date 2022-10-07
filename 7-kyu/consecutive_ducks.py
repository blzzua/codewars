# https://www.codewars.com/kata/5dae2599a8f7d90025d2f15f

from math import log
def consecutive_ducks(n):
    power_of_two = log(n)/log(2)
    return  int(power_of_two) != power_of_two


