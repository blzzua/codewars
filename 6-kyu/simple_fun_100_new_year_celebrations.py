# https://www.codewars.com/kata/589816a7d07028ac5c000016

def new_year_celebrations(takeoff_time, minutes):
    hh, mm = map(int, takeoff_time.split(':'))
    min_left = (24 * 60 - hh * 60 - mm) % (24 * 60)
    prev = 0
    res = 0
    for m in minutes:
        if min_left - prev >= 0 and m >= min_left:
            res += 1
        min_left += 60
        prev = m

    if len(minutes) > 0 and min_left < minutes[-1]:
        res += 0
    else:
        res += 1
    return res
