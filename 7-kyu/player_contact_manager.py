# https://www.codewars.com/kata/5b203de891c7469b520000b4

def player_manager(players):
    if players:
        l = players.split(', ')
        return [{'player': p, 'contact': int(c)} for p,c in zip(l[::2],l[1::2])]
    else:
        return []

