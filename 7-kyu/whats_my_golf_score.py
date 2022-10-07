# https://www.codewars.com/kata/59f7a0a77eb74bf96b00006a

def golf_score_calculator(par_string, score_string):
    return sum(map(int,score_string))-sum(map(int,par_string))

