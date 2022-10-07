# https://www.codewars.com/kata/566044325f8fddc1c000002c

def even_chars(st): 
    if 2 <= len(st) < 100:
        return [c for i, c in enumerate(st) if i % 2 ]
    else:
        return 'invalid string'
        
    

