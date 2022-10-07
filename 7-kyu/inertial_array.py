# https://www.codewars.com/kata/59a151c53f64cdd94c00008f

'''
  function name:- is_inertial
  input:- integer array
  ouput:- true if array is inertial false otherwise.
'''
def is_inertial(arr):
    odds = [i for i in arr if i % 2]
    evens = [i for i in arr if i % 2 == 0]
    last_evens = sorted(evens)[-2:]
    return len(odds)>0 and max(arr) in evens and (not last_evens[:-1] or min(odds) > last_evens[-2])
        

