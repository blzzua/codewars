# https://www.codewars.com/kata/584cfac5bd160694640000ae

def domino_reaction(s):
    l = len(s)
    if l == 0:
        return s
    sp = s.find(' ') if s.find(' ') >= 0 else l
    bp = s.find('/') if s.find('/') >= 0 else l
    break_pos = min((sp,bp))
    if break_pos < l or s[0] == '|':
        return s[:break_pos].replace('|','/') + s[break_pos:]
    else:
        return s
