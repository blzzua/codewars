# https://www.codewars.com/kata/57f75cc397d62fc93d000059

def calc(x):
    return sum([6 if '7' in str(ord(c)) else 0 for c in x])


