# https://www.codewars.com/kata/628e6f112324192c65cd8c97

def prescribe(d,a,b):
    res = 0
    max_a = d//a
    for i in range(max_a+1):
        a_val = a * i
        attemtp = a_val + (d - a_val) // b * b
        if res < attemtp:
            res = attemtp
    return res
