# https://www.codewars.com/kata/559d7951ce5e0da654000073

def alternate_sq_sum(arr):
    return sum(k**2 if i%2 else k for i,k in enumerate(arr))
    

