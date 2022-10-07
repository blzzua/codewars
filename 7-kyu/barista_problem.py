# https://www.codewars.com/kata/6167e70fc9bd9b00565ffa4e

def barista(coffees):
    time = ret = 0
    for i in sorted(coffees):
        time, ret = time + i + 2, ret + time + i 
    return ret


