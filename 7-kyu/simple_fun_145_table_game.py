# https://www.codewars.com/kata/58aa7f18821a769a7d000190

def table_game(table):
    t = [ table[i][j] for i in range(3) for j in range(3)]
    a, b, c, d = t[0], t[2], t[6], t[8]
    if a + b == t[1] \
        and a + c == t[3] \
        and b + d == t[5] \
        and c + d == t[7] \
        and a + b + c + d == t[4]:
        return [a,b,c,d]
    else:
        return [-1]
