# https://www.codewars.com/kata/525caa5c1bf619d28c000335

import numpy as np
def check_winner(A, pretendent):
    if np.any(np.all(np.lib.stride_tricks.sliding_window_view(A, (1, 3)) == pretendent, axis=-1)):
        return True # rows
    if np.any(np.all(np.lib.stride_tricks.sliding_window_view(A, (3, 1)).reshape(-1, 3) == pretendent, axis=1)):
        return True # cols
    if np.all(np.fliplr(A).diagonal() == pretendent) or np.all(np.diagonal(A) == pretendent): 
        return True # diag
    return False

def is_solved(board):
    A = np.array(board)
    win_x_arr = np.array([1,1,1])
    win_y_arr = np.array([2,2,2])
    if check_winner(A, win_x_arr):
        return 1
    if check_winner(A, win_y_arr):
        return 2
    if np.any(A == 0):
        return -1
    return 0
