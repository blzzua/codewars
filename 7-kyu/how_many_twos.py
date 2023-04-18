# https://www.codewars.com/kata/56aed5db9d5cb55de000001c

def two_count(n):
    i = 0
    for i in range(100):
        q = n // 2
        if  q  * 2 == n:
            n = q
            i+=1
        else:
            return i
  
