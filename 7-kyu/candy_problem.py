# https://www.codewars.com/kata/55466644b5d240d1d70000ba

def candies(s):
    if not s or len(s) == 1:
        return -1
    ss = sum(s)
    ll = len(s)
    max_  = max(s)
    return ll  * max_ - ss 
