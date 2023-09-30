# https://www.codewars.com/kata/56bb9b7838dd34d7d8001b3c
from scipy.ndimage import label
import numpy as np

def has_exit(maze):
    try:
        maze = np.array(list(map(list,maze)))
    except ValueError:
        return True            # True on failed maze? idk
    newshape = np.array(maze.shape) + np.array((2,2))
    if newshape.min() <= 3:
        return True            # simplest case
    bordered = np.full(shape=newshape, fill_value=' ', dtype='<U1')
    bordered[1:-1, 1:-1] = maze
    kates_coord = (bordered == 'k').nonzero()
    if len(kates_coord[0]) != 1:
        raise ValueError('There should be no multiple Kates')
    startcoord = [v[0] for v in kates_coord]
    bordered[startcoord[0],startcoord[1]] = ' '
    floodpath = label(bordered==bordered[startcoord[0],startcoord[1]])[0]
    return floodpath[0,0] == floodpath[startcoord[0],startcoord[1]]

