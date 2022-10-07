# https://www.codewars.com/kata/55ed875819ae85ca8b00005c

def multiply_and_filter(seq, multiplier): 
    return [i*multiplier for i in seq if type(i) in (int,float)]

