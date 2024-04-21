# https://www.codewars.com/kata/5b6183066d0db7bfac0000bb

import re

def memesorting(meme):
    patterns = { 'Roma': r'b[^u]*u[^g]*g',
                'Maxim': r'b[^o]*o[^o]*o[^m]*m', 
                'Danik': r'e[^d]*d[^i]*i[^t]*t[^s]*s' }
    meme = meme.lower()
    res = [ (re.search(pattern,meme).end() - re.search(pattern,meme).start(), name) 
           for name, pattern in patterns.items() if re.search(pattern,meme)] 
    if res:
        return min(res)[1]
    else:
        return 'Vlad'
    
