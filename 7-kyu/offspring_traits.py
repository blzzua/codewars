# https://www.codewars.com/kata/5b011461de4c7f8d78000052

def bear_fur(bears):
    b1, b2 = sorted([*bears])
    if b1 == b2:
        return b1
    furmap = {('black', 'brown'): 'dark brown',
              ('black', 'white'): 'grey',
              ('brown', 'white'): 'light brown'}
    return furmap.get( (b1, b2), 'unknown')
