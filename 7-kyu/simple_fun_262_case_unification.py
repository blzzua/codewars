# https://www.codewars.com/kata/59126cd3379de6ca5f00019c

def case_unification(s):
    return s.upper() if  sum(1 if c.isupper() else -1  for c in s) > 0 else s.lower()
    
        
        

