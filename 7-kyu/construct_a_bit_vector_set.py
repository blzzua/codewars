# https://www.codewars.com/kata/52f5424d0531259cfc000d04

def sort_by_bit(seq):
    return sum(2**b for b in seq)


