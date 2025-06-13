# https://www.codewars.com/kata/59eea9a13d09a75fd10002c5

def count_binary(s1, s2):
    l = len(s1)
    return sum(s1 == s2[i:i+l] for i in range(len(s2) - l+1))
