# https://www.codewars.com/kata/59cfc000aeb2844d16000075

def capitalize(s):
    return [''.join(c.lower() if i % 2 == 1 else c.upper() for i,c in enumerate(s)),
        ''.join(c.lower() if i % 2 == 0 else c.upper() for i,c in enumerate(s))]
    
        

