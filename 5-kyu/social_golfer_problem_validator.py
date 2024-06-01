# https://www.codewars.com/kata/556c04c72ee1147ff20000c9

from collections import Counter
from collections import defaultdict
def valid(a):
    N = len(''.join(a[0]))
    G = len(a[0])
    D = len(a)
    # rule 1 that each golfer plays exactly once every day
    for line in a:
        if not(len(set(''.join(line))) == len(''.join(line)) == N):
            print('each golfer plays exactly once every day')
            return False
    
    for line in a:
        if len(line) != G:
            print('# that the number the groups is not the same every day')
            return False # that the number and size of the groups is the same every day
    if not len(set(Counter(''.join([''.join(line) for line in a ])).values())) == 1:
        return False # detect an unknown player, can detect days with different group sizes

    played = defaultdict(list)
    for line in a:
        for play in line:
            for player in list(play):
                today_play = list(play)
                today_play.remove(player)
                for comp in today_play:
                    if comp in played[player]:
                        # print(f'DEBUG: in {play=} the {player=} already played with {comp=}: {played[player]}')
                        return False
                    else:
                        played[player].append(comp)
    return True
