# https://www.codewars.com/kata/5dfd129673aa2c002591f65d

from math import prod

def score(game):
    return sum(map(prod,game.outcomes))

def find_best_game(games):
    return max(games, key=score).name
