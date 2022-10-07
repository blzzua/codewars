# https://www.codewars.com/kata/5ae7e3f068e6445bc8000046

def next_happy_year(year):
    while True:
        year += 1
        if len(set(str(year))) == 4:
            break
    return year

