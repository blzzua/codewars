# https://www.codewars.com/kata/56eb0be52caf798c630013c0

from datetime import  date
def unlucky_days(year):
    return sum(1 for i in range(1,13) if date(year,i,13).weekday()==4)


