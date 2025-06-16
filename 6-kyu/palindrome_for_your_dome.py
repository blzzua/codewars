# https://www.codewars.com/kata/53046ceefe87e4905e00072a

def palindrome(string):
    st = [c.lower() for c in string if c.isalnum()]
    return st == st[::-1]
