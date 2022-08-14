# https://www.codewars.com/kata/5d1e1560c193ae0015b601a2

def count(a, t, x):
    res = 0
    for i in a:
        if x == 0:
            if i == t:
                res+=1
        else:
            if abs(i-t) % x == 0:
                res+=1
    return res

  
  
