# https://www.codewars.com/kata/5c15dd0fb48e91d81b0000c6

def team_comp(heroes):
    if len(heroes) != 6 or len(set(heroes)) != 6:
        raise InvalidTeam
    res = [0, 0, 0]
    for hero in heroes:
        if hero in TANK:
            res[0] += 1
        elif hero in DAMAGE:
            res[1] += 1
        elif hero in SUPPORT:
            res[2] += 1
    return res

