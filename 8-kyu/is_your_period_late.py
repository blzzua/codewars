# https://www.codewars.com/kata/578a8a01e9fd1549e50001f1

from datetime import date, timedelta
def period_is_late(last,today,cycle_length):
    if  abs(last - today) <= timedelta(days=cycle_length) :
        return False
    else:
        return True


