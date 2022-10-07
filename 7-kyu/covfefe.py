# https://www.codewars.com/kata/592fd8f752ee71ac7e00008a

def covfefe(s):
    if 'coverage' in s:
        return s.replace('coverage', 'covfefe')
    else:
        return s + ' covfefe'

