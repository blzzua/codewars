# https://www.codewars.com/kata/541837036d821665ee0006c2
def get_required(player,enemy):
    X = sum(player)
    Y = sum(enemy)
    Z = X - Y
    if Z >= 6:
        return 'Auto-win'
    if Z <= -6:
        return 'Auto-lose'
    return {-5: 'Pray for a tie!',
        -4: '(1..1)',
        -3: '(1..2)',
        -2: '(1..3)',
        -1: '(1..4)',
        0: 'Random',
        1: '(6..6)',
        2: '(5..6)',
        3: '(4..6)',
        4: '(3..6)',
        5: '(2..6)'}[Z]
    if X > Y:
        return f'({Z+7}..6)'
    else:
        return f'(1..{Z+5})'
