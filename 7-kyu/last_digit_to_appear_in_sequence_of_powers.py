# https://www.codewars.com/kata/5ccfcfad7306d900269da53f

def LDTA(n):
    res = dict() # since dict is like sorted set
    for cnt in range(1,25):
        c = n**cnt
        ints = [ int(d) for d in str(c) ]
        for i in ints: 
            res[i] = None
            if len(res) >= 10:
                return list(res.keys())[-1]
    return None
