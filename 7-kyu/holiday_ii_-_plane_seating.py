# https://www.codewars.com/kata/57e8f757085f7c7d6300009a

def plane_seat(a):
    raw_row, seat = a[:-1], a[-1]
    row = int(raw_row)
    if row > 60 or seat not in 'ABCDEFGHK':
        return 'No Seat!!'
    row_pos = {row <= 60: 'Back', row <= 40: 'Middle',  row <= 20: 'Front'}[True]
    seat_pos = {'A': 'Left', 'B': 'Left', 'C': 'Left',
                'D': 'Middle', 'E': 'Middle', 'F': 'Middle',
                'G': 'Right', 'H': 'Right', 'K': 'Right'}[seat]
    return f'{row_pos}-{seat_pos}'
