# https://www.codewars.com/kata/58f0ba42e89aa6158400000e

def fold_to(distance):
    if distance < 0:
        return None
    c = 0
    while distance >= 0.0001 :
        distance = distance /2
        c += 1
    return c 
