# https://www.codewars.com/kata/566fd169d39cf89e1e000044

def league_calculate(team1, team2, result, league_table):
    for i, (team, score) in enumerate(league_table):
        if team == team1:
            t1i = i
        if team == team2:
            t2i = i
    if result == 'win':
        league_table[t1i][1] += 3
    elif result == 'draw':
        league_table[t1i][1] += 1
        league_table[t2i][1] += 1
    
    league_table=sorted(league_table, key=lambda x: (-x[1], x[0]))
    return league_table

