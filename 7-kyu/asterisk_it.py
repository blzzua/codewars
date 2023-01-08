# https://www.codewars.com/kata/5888cba35194f7f5a800008b

def asterisc_it(n): 
    if isinstance(n,list):
        n = ''.join(map(str,n))
    if isinstance(n,int):
        n = str(n)
    res = n[0]
    for a,b in zip(n,n[1:]):
        if a in '02468' and b in '02468':
            res+="*"
        res+=b
    return res
            
