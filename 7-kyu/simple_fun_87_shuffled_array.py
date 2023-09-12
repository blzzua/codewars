# https://www.codewars.com/kata/589573e3f0902e8919000109

def shuffled_array(s):
    S = sum(s)
    for i in s:
        if S - i == i:
            s.remove(i)
            return sorted(s)
