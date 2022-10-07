# https://www.codewars.com/kata/55ccdf1512938ce3ac000056

import re
def is_lock_ness_monster(string):
    return bool(re.findall(r'(three fifty)|(tree fiddy)|(3\.50)', string))
    

