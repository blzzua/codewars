# https://www.codewars.com/kata/576bb3c4b1abc497ec000065

def compare(s1,s2):
    if s1 is None or not s1.isalpha():
        s1 = ''
    if s2 is None or not s2.isalpha():
        s2 = ''
    return sum(map(ord,s1.upper()))==sum(map(ord,s2.upper()))

