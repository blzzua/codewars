# https://www.codewars.com/kata/583a8bde28019d615a000035

def find_odd_names(lst): 
    return [o for o in lst if sum(ord(i) for i in o['firstName'] ) % 2 == 1]
    
