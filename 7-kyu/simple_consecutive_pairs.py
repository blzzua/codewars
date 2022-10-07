# https://www.codewars.com/kata/5a3e1319b6486ac96f000049

def pairs(ar):
    return sum(abs(a-b) == 1 for a,b in zip(ar[0::2], ar[1::2]))

