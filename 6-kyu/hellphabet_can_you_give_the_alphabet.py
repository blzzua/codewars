# https://www.codewars.com/kata/62dcbe87f4ac96005f052962
ALPHABET = str().join(c for c in sorted(set(str().join(str().join(dir(type(i))) for i in (vars().values())))) if c.isalpha())

# clever methods like
## chr(i) for i in range(len(str( ... )))    btw: str(credits) has 158 chars long
