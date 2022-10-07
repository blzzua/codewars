# https://www.codewars.com/kata/546f922b54af40e1e90001da

from string import ascii_letters
def alphabet_position(text):
    alpha = {c: str(i) for i,c in enumerate(ascii_letters,1)}
    return ' '.join(map(lambda c: alpha.get(c.lower(),''), text)).strip()

