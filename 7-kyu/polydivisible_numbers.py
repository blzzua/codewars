# https://www.codewars.com/kata/5e4217e476126b000170489b

def polydivisible(x):
    if x < 10:
        return True
    s = str(x)
    for i in range(1,len(s)+1):
        if int(s[:i]) % i:
            return False
    return True
