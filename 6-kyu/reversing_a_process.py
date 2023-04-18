# https://www.codewars.com/kata/5dad6e5264e25a001918a1fc

from string import ascii_lowercase as al
import re
def decode(r):
    num = re.findall('\d+',r)
    if not num:
        return 'Impossible to decode'
    num_s  = num[0]
    num = int(num_s)
    al_rmap = {i:c for i,c in enumerate(al)}
    decode_map ={ al_rmap.get(i * num % 26) : al_rmap.get(i)  for i in range(26) }
    if len(decode_map) < 26:
        return 'Impossible to decode' 
    res = ''.join(decode_map.get(c, '') for c in  r[len(num_s):])
    return res
    
