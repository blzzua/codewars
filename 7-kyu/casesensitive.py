# https://www.codewars.com/kata/5a805631ba1bb55b0c0000b8

def case_sensitive(s):
    return [all(map(str.islower, s)), [*(filter(str.isupper, s))]]

