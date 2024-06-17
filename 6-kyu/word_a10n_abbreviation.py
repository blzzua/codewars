# https://www.codewars.com/kata/5375f921003bf62192000746

from itertools import groupby
from string import ascii_letters

def abbreviate(s):
    print(s)
    res = []
    for is_separator, data in groupby(s, key=lambda x: x in ascii_letters):
        if is_separator:
            word_list = list(data)
            if len(word_list) < 4:
                res.append(''.join(word_list))
            else:
                res.append(word_list[0] + str(len(word_list)-2) + word_list[-1])
        else:
            res.append(''.join(data))
    return ''.join(res)
