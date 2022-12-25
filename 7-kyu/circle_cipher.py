# https://www.codewars.com/kata/634d0723075de3f97a9eb604

def encode(s:str) -> str:
    if not s:
        return ''
    if len(s) == 1:
        return s

    res = s[0]
    h = len(s)//2
    for i in range(1,h):
        res+=s[-i]
        res+=s[i]
    if len(s) % 2 == 0:
        res+=s[h]
    else:
        res+=s[-h]
        res+=s[h]
    return res        

# clever but recurive solution:  return s and s[0]+encode(s[:0:-1])

def decode(s:str) -> str:
    if not s:
        return ''
    return s[::2]+s[1::2][::-1]
