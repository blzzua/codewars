# https://www.codewars.com/kata/5620dc848370b4ad750000a1

def triangular_range(start, stop):
    res, i = {}, 1
    while True:
        tn = ((i+1)*i)//2
        if start <= tn <= stop:
            res[i] = tn
        elif tn > stop:
            return res
        i+=1
