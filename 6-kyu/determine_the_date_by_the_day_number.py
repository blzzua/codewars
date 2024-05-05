# https://www.codewars.com/kata/602afedfd4a64d0008eb4e6e

MONTH= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def get_day(day, is_leap): 
    DM = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap:
        DM[1] = 29
    m = 0
    while day > DM[m]:
        day -= DM[m]
        m+=1
    return f'{MONTH[m]}, {day}'
  
