# https://www.codewars.com/kata/59126992f9f87fd31600009b

def whoseMove(lastPlayer, win):
    return ["white", "black"][(lastPlayer == "black") == win]

