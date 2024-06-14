# https://www.codewars.com/kata/56419475931903e9d1000087

from string import ascii_uppercase as up
from string import ascii_lowercase as lo
def one_down(txt):
    if not isinstance(txt, str):
        return 'Input is not a string'
    tr = str.maketrans(up[1:] + up[:1] + lo[1:] + lo[:1], up + lo)
    return txt.translate(tr)
    
