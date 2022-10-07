# https://www.codewars.com/kata/58287977ef8d4451f90001a0

def is_same_language(lst): 
    return len(set([o['language'] for o in lst])) == 1

