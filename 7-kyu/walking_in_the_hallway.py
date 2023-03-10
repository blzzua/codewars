# https://www.codewars.com/kata/6368426ec94f16a1e7e137fc

import re
def contact(hallway):
    fnd = [ (m.span()[0], m.group()) for m in re.finditer('<|>', hallway)]
    collisions = [(b[0]-a[0]+1) for a, b in zip(fnd,fnd[1:]) if a[1] == '>' and b[1] == '<']
    if collisions:
        return max(min(collisions)//2, 1)
    else:
        return -1
