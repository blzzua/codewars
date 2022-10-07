# https://www.codewars.com/kata/54fdadc8762e2e51e400032c

def my_parse_int(string):
    if len([x for x in string.strip() if not x.isdigit()]) == 0:
        return int(string) 
    else:
        return 'NaN'

