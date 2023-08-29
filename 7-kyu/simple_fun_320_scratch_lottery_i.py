# https://www.codewars.com/kata/594a1822a2db9e93bd0001d4

def scratch(lottery):
    win = 0
    for ticket in lottery:
        t1,t2,t3,v = ticket.split()
        if t1 == t2 and t2 == t3:
            win += int(v)
    return win
