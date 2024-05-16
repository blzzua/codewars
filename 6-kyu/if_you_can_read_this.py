# https://www.codewars.com/kata/586538146b56991861000293

from preloaded import NATO # NATO['A'] == 'Alfa', etc
for c in '?!.,':
    NATO[c] = c

def to_nato(words : str) -> str:
    return ' '.join(NATO.get(c.upper()) for c in words.upper() if c in NATO)
