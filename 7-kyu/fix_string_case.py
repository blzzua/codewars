# https://www.codewars.com/kata/5b180e9fedaa564a7000009a

def solve(s):
    if sum(map(str.isupper, s)) * 2 > len(s):
        return s.upper()
    else:
        return s.lower()

