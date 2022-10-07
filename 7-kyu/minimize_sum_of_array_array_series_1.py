# https://www.codewars.com/kata/5a523566b3bfa84c2e00010b

def min_sum(arr):
    arr = sorted(arr) 
    return sum([ a*b for a,b, _  in zip(arr,arr[::-1], range(len(arr)//2))])

