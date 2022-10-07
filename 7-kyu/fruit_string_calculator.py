# https://www.codewars.com/kata/57b9fc5b8f5813384a000aa3

import re
def calculate(string):
    a,op,b = re.findall(r'\w+ has (\d+) [\w ]+ and (loses|gains) (\d+)',string)[0]
    if op == 'loses':
        return int(a) - int(b)
    elif op == 'gains':
        return int(a) + int(b)
    
    
    

