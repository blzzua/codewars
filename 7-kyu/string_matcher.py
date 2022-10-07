# https://www.codewars.com/kata/565ce4ab24ef4aee6a000074

def is_matching(*s):
    s = [*map(lambda s: s.replace(' ','').lower(),s)]
    return sorted(s[0]) == sorted(s[1]+s[2])


