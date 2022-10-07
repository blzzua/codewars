# https://www.codewars.com/kata/569218bc919ccba77000000b

from datetime import datetime, timedelta
def date_nb_days(a0, a, p):
    interest = p/36000
    c = 0
    while a0 < a:
        a0 += a0 * interest
        c += 1
    return (datetime(2016, 1, 1) + timedelta(days=c)).strftime("%Y-%m-%d")    


