# https://www.codewars.com/kata/5d0d1c14c843440026d7958e

def find_needed_guards(k):
    res = 0
    for i,(a,b) in enumerate(zip(k,k[1:]),1):
        if not(a or b):
            res +=1
            k[i] = True
    return res
