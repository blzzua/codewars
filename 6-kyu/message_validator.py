# https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc

import re
def is_a_valid_message(message):
    valid = all(int(n) == len(w) for n,w in re.findall(r'(\d+)([a-z]+)',message, flags = re.I))
    # in the name of readability
    if valid and re.match(r'((\d+)([a-z]+))*$',message, flags = re.I):
        return True
    else:
        return False


# clever:
import re
def is_a_valid_message(message):
    return all(n and int(n) == len(s) for n, s in re.findall("(\d*)(\D*)", message)[:-1])
  
# best practice wo re:
def is_a_valid_message(message):
    size = 0
    count = 0
    for c in message:
        if c.isnumeric():
            if count == 0:
                size = size * 10 + int(c)
            else:
                if count != size:
                    return False
                count = 0
                size = int(c)
        else:
            count = count + 1
    return count == size
