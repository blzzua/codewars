#  https://www.codewars.com/kata/55ee3ebff71e82a30000006a

from string import ascii_uppercase as alphabet

def title_to_number(title):
    alphabet_map = {k:v for v,k in enumerate(alphabet,1)}
    alphabet_len = len(alphabet)
    return sum(alphabet_len ** i * alphabet_map.get(k)  for i, k in enumerate(title[::-1]))
