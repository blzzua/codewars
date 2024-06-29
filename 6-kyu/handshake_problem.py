# https://www.codewars.com/kata/5574835e3e404a0bed00001b

def get_participants(handshakes):
    i = 0
    res = 0
    while i < handshakes:
        i += res
        res += 1
    return res

# clever math:
math.ceil((1 + math.sqrt(1 + 8 * n)) / 2) 

