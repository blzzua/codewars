# https://www.codewars.com/kata/5c744111cb0cdd3206f96665

def solution(to_cur, value, xccy = 1.1363636 ):
    if to_cur == 'USD':
         return ['${:,.02f}'.format(round(v * xccy, 2)) for v in value]
    elif to_cur == 'EUR':
         return ['{:,.02f}€'.format(round(v / xccy, 2))for v in value]
