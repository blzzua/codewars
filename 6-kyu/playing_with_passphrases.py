# https://www.codewars.com/kata/559536379512a64472000053

from string import ascii_lowercase as al

def play_pass(s, n):
    tr_map_letter = str.maketrans(al, (al+al)[n:n+26])
    tr_map_digit = str.maketrans('0123456789','9876543210')
    res = s.lower().translate(tr_map_letter).translate(tr_map_digit)              # 1, 2, 3
    res = ''.join([c.lower() if i % 2 else c.upper() for i, c in enumerate(res)]) # 4
    return res[::-1]                                                              # 5

