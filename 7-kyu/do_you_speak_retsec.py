# https://www.codewars.com/kata/5516ab668915478845000780

def reverse_by_center(s):
    m = len(s) // 2
    return s[-m:] + ( s[m] if len(s) % 2 else '' ) +  s[:m]
