# https://www.codewars.com/kata/571b2ee08d8c9c0d160014ec

def sexy_name(name):
    score = sum(SCORES.get(c.upper(),0) for c in name)
    return ['NOT TOO SEXY', 'PRETTY SEXY', 'VERY SEXY', 'THE ULTIMATE SEXIEST'][(score > 60)+ (score > 300) + (score > 599)]


