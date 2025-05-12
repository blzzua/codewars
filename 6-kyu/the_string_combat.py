# https://www.codewars.com/kata/56e23f98bf8f6e9aed000367

from string import ascii_lowercase, ascii_uppercase
scores = ' '+ ascii_lowercase + ascii_uppercase

def combat(s1, s2):
    l1 = [scores.index(c) for c in s1][::-1]
    l2 = [scores.index(c) for c in s2][::-1]
    while l1 and l2:
        c1 = l1.pop()
        c2 = l2.pop()
        if c1 > c2:
            left1 = round(c1 / 3)
            if left1: 
                l1.append(left1)
        elif c1 < c2:
            left2 = round(c2 / 3)
            if left2:
                l2.append(left2)
    if l1:
        winner = 'Winner: s1(' + ''.join(map(lambda x: scores[x], l1[::-1])) +')'
    elif l2:
        winner = 'Winner: s2(' + ''.join(map(lambda x: scores[x], l2[::-1])) +')'
    else:
         winner = "Draw"
    return winner
