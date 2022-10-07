# https://www.codewars.com/kata/558dd9a1b3f79dc88e000001

def find_dup(arr):
    return sum(arr) - sum(set(arr))
    

