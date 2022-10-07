# https://www.codewars.com/kata/5828713ed04efde70e000346

from collections import Counter
def count_languages(lst): 
    return dict(Counter(o.get('language') for o in lst))
        

