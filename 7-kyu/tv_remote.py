# https://www.codewars.com/kata/5a5032f4fd56cb958e00007a

keyboard="""a   b   c   d   e   1   2   3
f   g   h   i   j   4   5   6
k   l   m   n   o   7   8   9
p   q   r   s   t   .   @   0
u   v   w   x   y   z   _   /"""

def tv_remote(word):
    cost = {c: (i,j) for i, row in enumerate(keyboard.splitlines()) for j,c in enumerate(row.split()) }
    res = 0
    ok_button_cost = 1
    for a,b in zip('a'+word, word):
        ca = cost.get(a)
        cb = cost.get(b)
        res += abs(ca[0]-cb[0]) + abs(ca[1]-cb[1]) + ok_button_cost
    return res

