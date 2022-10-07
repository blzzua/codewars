# https://www.codewars.com/kata/588e68aed4cff457d300002e

def turn(current, target):
    dirs_right = 'NESW'
    orientation = {(c,t): 'right' for c,t in zip(dirs_right, dirs_right[1:]+dirs_right[0])}

    dirs_left = dirs_right[::-1]
    for c,t in zip(dirs_left, dirs_left[1:]+ dirs_left[0]):
        orientation[(c,t)] = 'left'

    return orientation.get((current, target))


