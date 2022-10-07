# https://www.codewars.com/kata/5bc9951026f1cdc77400011c

from collections import Counter
def baby_count(x):
    c = Counter(x.lower()) 
    cc = min(c.get('b',0)//2, c.get('a',0), c.get('y',0))
    return cc if cc > 0 else 'Where\'s the baby?!'

