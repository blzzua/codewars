# https://www.codewars.com/kata/582e0450fe38013dbc0002d3

import re
def regex_tic_tac_toe_win_checker(board):
    return any(re.findall(r.replace('1','(X|O)').replace('2','\\1'), board) for r in ['......122', '..1.2.2..', '...122...',  '122......',  '1..2..2', '1...2...2', '1..2..2'])

# r'......(X|O)\1\1', r'..(X|O).\1.\1..', r'...(X|O)\1\1...',  r'(X|O)\1\1......',  r'(X|O)..\1..\1', r'(X|O)...\1...\1', r'(X|O)..\1..\1'    

