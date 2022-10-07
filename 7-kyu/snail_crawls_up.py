# https://www.codewars.com/kata/5b93fecd8463745630001d05

def snail(column, day, night):
    if day >= column:
        return 1
    else:
        return int(1.99999 + (column-day)/(day-night)) 

