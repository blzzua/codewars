# https://www.codewars.com/kata/570564e838428f2eca001d73

import re
def chuck_push_ups(st): 
    if not isinstance(st, str):
        return 'FAIL!!'
    else:
        return max((int(re.sub(r'[\D2-9]', '', st),2) for st in re.findall(r'\S+[01]\S+',st)), default='CHUCK SMASH!!')


