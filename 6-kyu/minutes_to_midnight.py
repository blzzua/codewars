# https://www.codewars.com/kata/58528e9e22555d8d33000163

def minutes_to_midnight(d):
    res = round( 60 * 24 - (d.timestamp() % 86400) / 60 ) 
    if res == 1:
        return '1 minute'
    else:
        return f'{res} minutes'
