# https://www.codewars.com/kata/65128732b5aff40032a3d8f0

def neutralise(s1, s2):
    return ''.join(ch1 if ch1 == ch2 else '0' for ch1, ch2 in zip(s1, s2))
