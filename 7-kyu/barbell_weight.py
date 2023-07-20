# https://www.codewars.com/kata/6400aa17431f2d89c07eea75

w_map = {'R': 25 , 'B': 20 , 'Y': 15 , 'G': 10 , 'W': 5  ,  'r': 2.5, 'b': 2  ,  'y': 1.5, 'g': 1  ,  'w': 0.5, 'c': 2.5,} 
bar = 20

def barbell_weight(barbell):
    return bar + sum(w_map.get(d, 0)for d in barbell)
