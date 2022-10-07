# https://www.codewars.com/kata/55c353487fe3cc80660001d4

def capitals_first(text):
    return ' '.join(sorted(filter(lambda w:w[0].isalpha(), text.split()), key=lambda w: w[0].islower()))

