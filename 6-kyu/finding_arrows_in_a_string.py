# https://www.codewars.com/kata/63744cbed39ec3376c84ff4a

import re

def point(arrow):
    coef = 2 if '=' in arrow else 1
    return len(arrow) * coef

def arrow_search(string: str) -> int:
    r = re.findall('<(?:-+|=*)', string) 
    l = re.findall('(?:-+|=*)>', string) 
    return sum(map(point, l)) - sum(map(point, r))

# intresting fact that is autor solution is without regex
