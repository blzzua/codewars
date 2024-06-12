# https://www.codewars.com/kata/58a65945fd7051d5e1000041

from itertools import zip_longest 
def six_column_encryption(msg, cols = 6):
    return ' '.join(''.join(col).replace(' ','.') for col in zip(*zip_longest(*[iter(msg)] * cols, fillvalue=' ')))
