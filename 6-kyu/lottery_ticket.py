# https://www.codewars.com/kata/57f625992f4d53c24200070e

def bingo(ticket,win):
    wins = 0
    for char_list, char_num in ticket:
        if chr(char_num)  in char_list:
            wins += 1 
    if wins >= win:
        return 'Winner!'
    else:
        return 'Loser!'
