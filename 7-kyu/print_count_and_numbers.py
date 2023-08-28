# https://www.codewars.com/kata/559af787b4b8eac78b000022

from itertools import groupby
def count_me(data):
    if data.isnumeric():
        return ''.join([str(len([*v])) + g for g,v in groupby(data)])
    else:
        return ''
