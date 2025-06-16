# https://www.codewars.com/kata/53ea07c9247bc3fcaa00084d

from itertools import groupby
from functools import lru_cache

# reuse solution from previuos attempts
@lru_cache(10000)
def look_and_say_routine(data='1', maxlen=5):
    res = ''
    for g, data in groupby(data):
        res = res + str(len(list(data))) + g
    if maxlen==1:
        return res
    else:
        return look_and_say_routine(data=res, maxlen=maxlen-1)
    
    
def look_and_say(data='1', maxlen=5):
    res = []
    for i in range(1,maxlen+1):
        res.append(look_and_say_routine(data=data, maxlen=i))
    return res

