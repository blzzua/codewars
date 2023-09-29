# https://www.codewars.com/kata/5411c4205f3a7fd3f90009ea

from itertools import groupby
def string_parse(string):
    if not isinstance(string, str):
        return 'Please enter a valid string'
    res = ''
    for g, cg in groupby(string):
        data = ''.join(list(cg))
        if len(data) <= 2:
            res += data
        if len(data) > 2:
            res += data[:2] + '[' + data[2:] + ']'
    return res

# clever regex substution: re.sub(r'(\w)\1(\1+)', r'\1\1[\2]', string) 
