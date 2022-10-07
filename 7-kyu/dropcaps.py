# https://www.codewars.com/kata/559e5b717dd758a3eb00005a

import re
def cap_routine(word):
    return word if len(word) <=2 else word.capitalize()

def drop_cap(str_):
    return ' '.join([cap_routine(word) for word in re.split(' ',str_)])


