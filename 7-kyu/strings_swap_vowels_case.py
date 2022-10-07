# https://www.codewars.com/kata/5803c0c6ab6c20a06f000026

def swap_vowel_case(st): 
    return ''.join(c.swapcase() if c in 'aeiouAEIOU' else c for c in st)
    

