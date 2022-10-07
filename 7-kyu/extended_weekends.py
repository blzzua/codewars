# https://www.codewars.com/kata/5be7f613f59e0355ee00000f
  
from datetime import date
def solve(a,b):
    res = []
    for y in range(a,b+1):
        for m in [1,3,5,7,8,10,12]:
            if date(y,m,1).weekday() == 4:
                res.append((m,y))
    return (date(a,res[0][0],1).strftime('%b'),
            date(a,res[-1][0],1).strftime('%b'),
            len(res))
