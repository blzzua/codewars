# https://www.codewars.com/kata/5663f5305102699bad000056

def mxdiflg(a1, a2):
    if a1 and a2:
        a1 = sorted(a1,key=len)
        a2 = sorted(a2,key=len)
        return  max( abs(len(a1[0])-len(a2[-1])), abs(len(a1[-1]) - len(a2[0])) )
    else:
        return -1
    

