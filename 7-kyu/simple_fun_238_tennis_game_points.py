# https://www.codewars.com/kata/590942d4efde93886900185a

def tennis_game_points(score): 
    alias = {'love':0,'15':1,'30':2,'40':3}
    return sum([alias.get(x,alias[score.split("-")[0]]) for x in score.split("-")])

