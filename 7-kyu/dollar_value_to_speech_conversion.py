# https://www.codewars.com/kata/5b23d98da97f02a5f4000a4c

def dollar_to_speech(value):
    if '-' in value:
        return 'No negative numbers are allowed!'
    d, c = (map(int, value.replace('$', '').split('.')))
    d_end = '' if d == 1 else 's'
    d_s = f'{d} dollar{d_end}' if d > 0 or (c == d ==0 ) else ''
    sep = ' and ' if (d and c) else ''
    c_end = '' if c == 1 else 's'
    c_s = f'{c} cent{c_end}' if c > 0 else ''
    return f'{d_s}{sep}{c_s}.'
