# https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1

def get_ages(s, d):
    a = (s + d) / 2
    b = s - a
    if all(i>= 0 for i in (a,b,s,d)):
        return  max(a,b), min(a,b)
    

