# https://www.codewars.com/kata/63f3c61dd27f3c07cc7978de

def compare(a, b):
    d1 = sorted(divmod(a,10))
    d2 = sorted(divmod(b,10))
    if d1 == d2:
        return "100%"
    if d1[0] == d2[0] or d1[1] == d2[1] or d1[0] == d2[1] or d1[1] == d2[0]:  
        return "50%"
    return "0%"
  
