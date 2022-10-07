# https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2

def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    return directions[(turn // 45 + directions.index(facing)) % 8]

