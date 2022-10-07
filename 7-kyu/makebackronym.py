# https://www.codewars.com/kata/55805ab490c73741b7000064

def make_backronym(acronym):
    return ' '.join(map(dictionary.get, acronym.upper()))

