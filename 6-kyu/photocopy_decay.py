# https://www.codewars.com/kata/5b6fcd9668cb2e282d00000f

from string import ascii_lowercase, ascii_uppercase
def generation_loss(orig, copy):
    if len(orig) != len(copy):
        return False

    degradation = '#+:. '
    possible = {}
    for char in ascii_uppercase:
        possible[char] = char
    for char in ascii_lowercase:
        possible[char] = char + char.upper()
    for char in degradation[::-1]:
        possible[char] = ascii_uppercase + ascii_lowercase + degradation[:degradation.index(char)] + char

    for co, cc in zip(orig, copy):
        if cc != co and not(co in list(possible.get(cc, ''))):
            return False
    return True

