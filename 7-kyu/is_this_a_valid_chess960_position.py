#  https://www.codewars.com/kata/61488fde47472d000827a51d

def is_valid(positions):
    king = positions.index('K')
    left, right, is_b, left_idx, right_idx  = (False, False, True, 0, 0)
    for i, c in enumerate(positions):
        if c == 'R':
            (left, right) = ((True, right) if i < king else (left, True) if i > king else (left, right))
        if c == 'B':
            right_idx = i
            left_idx, is_b = (i, False) if is_b else (left_idx, True)
    return all((left, right,left_idx % 2 != right_idx % 2))
