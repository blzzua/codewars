# https://www.codewars.com/kata/5af304892c5061951e0000ce

def bingo(card, numbers):
    card_numbers = []
    [card_numbers.extend(l) for l in  card[1:]]
    correct_numbers = [int(cell[1:]) for cell in numbers]

    winline = [0] * len(card_numbers)
    for i, number in enumerate(card_numbers):
        if number in correct_numbers or number == 'FREE SPACE':
            winline[i] = 1
    winmap = [winline[i::5] for i in range(5)]
    # print('\n'.join(''.join(map(str,line)) for line in winmap))
    if any([all(row) for row in winmap]): # somerow
        return True

    if any([all(col) for col in zip(*winmap)]): # somecol
        return True

    if all([winmap[i][i] for i in range(5)]) or all([winmap[4-i][i] for i in range(5)]): # diagonal
        return True
    
    return False

