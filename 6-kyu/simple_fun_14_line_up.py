# https://www.codewars.com/kata/5884658d02accbd0a7000039

def line_up(commands):
    norm, anti = 0, 0
    res = 0
    for cmd in commands:
        if cmd == 'L':
            norm = (norm + 1) % 4
            anti = (anti - 1) % 4
        elif cmd == 'R':
            norm = (norm - 1) % 4
            anti = (anti + 1) % 4
        elif cmd == 'A':
            norm = (norm + 2) % 4
            anti = (anti + 2) % 4
        if norm == anti: 
            res += 1
    return res

# optimization 
    identical_direction = True
    res = 0
    for cmd in commands:
        if cmd in ('L', 'R'):
            identical_direction = not identical_direction
         res += int(identical_direction)
    return res
