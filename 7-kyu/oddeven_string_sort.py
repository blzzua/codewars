# https://www.codewars.com/kata/580755730b5a77650500010c


def sort_my_string(s):
    t = sorted([(i%2,i,c) for i,c in enumerate(s)])
    p1 = ''.join([c for a,b,c in filter(lambda t: t[0]==0,t)])
    p2 = ''.join([c for a,b,c in filter(lambda t: t[0]==1,t)])
    return p1 + ' ' + p2

    

