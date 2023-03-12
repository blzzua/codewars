# https://www.codewars.com/kata/5a106ce7ffe75f4c200000f7/

import random

MAP = {}

def prepare():
    global MAP
    for i in range(10000+1):
        random.seed(i)
        MAP[(random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))] = i
prepare()
        
def find_random_seed(lst):
    return MAP.get( tuple(lst[0:4]) ) 
