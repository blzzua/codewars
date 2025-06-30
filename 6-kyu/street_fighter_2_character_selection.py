# https://www.codewars.com/kata/5853213063adbd1b9b0000be

def street_fighter_selection(fighters, initial_position, moves):
    pos = list(initial_position)
    res = []
    for move in moves:
        match move:
            case 'up':
                pos[0] = max(0, pos[0]-1 )
                res.append(fighters[pos[0]][pos[1]])
            case 'down':
                pos[0] = min(pos[0]+1, len(pos)-1 )
                res.append(fighters[pos[0]][pos[1]])
            case 'left':
                pos[1] = (len(fighters[0]) + pos[1]-1) % len(fighters[0])
                res.append(fighters[pos[0]][pos[1]])
            case 'right':
                pos[1] = (pos[1]+1) % len(fighters[0])
                res.append(fighters[pos[0]][pos[1]])     
    return res

