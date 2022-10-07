# https://www.codewars.com/kata/571c1e847beb0a8f8900153d

def rake_garden(garden):
    return ' '.join(w if w == 'rock' else 'gravel' for w in garden.split())

