# https://www.codewars.com/kata/634913db7611b9003dff49ad

import re
def purify(s: str) -> str:
    print(s)
    return ' '.join(re.sub(r'(\w?i+\w?)', '', s, 0, re.IGNORECASE).split())
