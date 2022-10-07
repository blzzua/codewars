# https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145

def bingo(array): 
    c = 0
    for i in [2,9,14,7,15]:
        if i in array:
            c+=1
    if c == 5:
        return "WIN"
    else:
        return "LOSE"

