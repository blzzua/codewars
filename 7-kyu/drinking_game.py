#  https://www.codewars.com/kata/5a491f0be6be389dbb000117

def game(*players):
    cur_bet = 0
    cur_player = 1
    players = list(players)
    player_names = ['Mike','Joe']
    if 0 in players:
        return "Non-drinkers can't play"
    while True:
        cur_bet+=1
        cur_player = 1 - cur_player
        players[cur_player] -= cur_bet
        if players[cur_player] < 0:
            return player_names[1-cur_player]

