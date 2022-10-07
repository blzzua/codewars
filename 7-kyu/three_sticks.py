# https://www.codewars.com/kata/57c1f22d8fbb9fd88700009b

def maxlen(L1,L2):
    m1, l2 = sorted( (L1,L2))
    return min(max(l2 /3, m1), l2 /2)

