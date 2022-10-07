# https://www.codewars.com/kata/57d29ccda56edb4187000052

def rpsls(pl1, pl2):
    win_pairs = {
    ('scissors', 'paper'),
    ('paper', 'rock'),
    ('rock', 'lizard'),
    ('lizard', 'spock'),
    ('spock', 'scissors'),
    ('scissors', 'lizard'),
    ('lizard', 'paper'),
    ('paper', 'spock'),
    ('spock', 'rock'),
    ('rock', 'scissors')}

    if pl1 == pl2:
        return 'Draw!'
    elif (pl1, pl2) in win_pairs:
        return 'Player 1 Won!'
    else:
        return 'Player 2 Won!'
    


