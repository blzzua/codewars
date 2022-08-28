# https://www.codewars.com/kata/580535462e7b330bd300003d

def play(g1,g2):
    if (g1,g2) in [("rock", "paper"), ("paper", "scissors"), ("scissors","rock")]:
        return -1
    if (g2,g1) in [("rock", "paper"), ("paper", "scissors"), ("scissors","rock")]:
        return 1
    return 0


def oracle(gestures):
    scores = {'rock':0, 'paper':0, 'scissors':0}
    for g1 in scores:
        for g2 in gestures:
            scores[g1]+=play(g1,g2)
    return '/'.join(item for item in scores if scores[item] > 0) or 'tie'
