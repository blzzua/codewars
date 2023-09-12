# https://www.codewars.com/kata/5e28b3ff0acfbb001f348ccc

def is_solved(board):
    size = len(board)
    return all(i == board[i // size][i % size]  for i in range(size * size))
